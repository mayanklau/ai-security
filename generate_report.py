import csv, os
from collections import Counter

folder = input("Enter project folder (e.g. projects/demo.testfire.net): ")
file_path = os.path.join(folder, "payloads_tagged.csv")
report_path = os.path.join(folder, "risk_summary.txt")

if not os.path.exists(file_path):
    print("Tagged file not found.")
    exit()

counter = Counter()

with open(file_path) as f:
    reader = csv.DictReader(f)
    for row in reader:
        tag = row.get("tag", "")
        for level in ["High", "Medium", "Low"]:
            if level.lower() in tag.lower():
                counter[level] += 1

summary = f"""
=== Risk Summary Report ===
Project: {folder}
High-Risk Payloads: {counter['High']}
Medium-Risk Payloads: {counter['Medium']}
Low-Risk Payloads: {counter['Low']}
"""

print(summary)

with open(report_path, "w") as rf:
    rf.write(summary)

print(f"Report saved to: {report_path}")
