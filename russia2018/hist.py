#!/usr/bin/env python3

import csv
import matplotlib.pyplot as plt
import json

koibs = json.loads(open("koibs_kegs.json").read())
sKoibs = set()
for k, v in koibs.items():
    for koib in v["koibs"]:
        sKoibs.add(k + str(koib))
print("#Koibs: %d" % len(sKoibs))

putinBins = [0]*101
putinKoibBins = [0]*101
with open("table_227_level_3.tsv", "r") as f:
    next(f)
    for line in f:
        row = line.strip().split("\t")
        total = int(row[3])
        votes = int(row[12])
        putin = int(row[18])
        region = row[0]
        number = int(row[2][5:])
        # print(total, votes, putin)
        assert votes <= total
        assert putin <= votes
        if votes:
            turnover = float(votes)/total
            putinRatio = float(putin)/float(votes)
            putinBin = int(100.0 * putinRatio)
            if region + str(number) in sKoibs:
                putinKoibBins[putinBin] += putin
            else:
                putinBins[putinBin] += putin

abins = []
for i in range(101):
    abins.append(i)

plt.clf()
plt.plot(abins, putinBins, color='red', label="Putin without KOIB")
plt.plot(abins, putinKoibBins, color='blue', label="Putin with KOIB")
plt.legend()
plt.suptitle("Russia")
plt.savefig("pAll.png", dpi=300)
plt.show()