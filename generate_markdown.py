import os, csv
from collections import Counter

folder = input("Enter full folder path (e.g. projects/demo.testfire.net/2024-04-01_19-42): ")
tag_file = os.path.join(folder, "payloads_tagged.csv")
md_file = os.path.join(folder, "risk_report.md")

if not os.path.exists(tag_file):
    print("❌ payloads_tagged.csv not found.")
    exit()

counter = Counter()
with open(tag_file) as f:
    reader = csv.DictReader(f)
    for row in reader:
        tag = row.get("tag", "").lower()
        for level in ["high", "medium", "low"]:
            if level in tag:
                counter[level] += 1

report = f"""# Risk Report

**Project:** `{folder}`

| Risk Level | Count |
|------------|-------|
| High       | {counter['high']} |
| Medium     | {counter['medium']} |
| Low        | {counter['low']} |

_This report is auto-generated after GPT-based payload tagging._
"""

print(report)

with open(md_file, "w") as f:
    f.write(report)

print(f"[✓] Markdown report saved: {md_file}")
