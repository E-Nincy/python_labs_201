# Use the csv module to read in and count the different file types.

import csv
from collections import defaultdict

file_type_totals = defaultdict(int)

with open("filecounts.csv", "r", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        for ext, count in row.items():
            if ext != "timestamp":
                file_type_totals[ext] += int(count)

# Total
for ext, total in file_type_totals.items():
    print(f"{ext}: {total}")
