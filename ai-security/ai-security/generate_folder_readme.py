import os
import csv
from collections import Counter

# Prompt for project folder path (example: projects/demo.testfire.net/2025-03-31_16-10)
folder = input("Enter full folder path (e.g. projects/demo.testfire.net/2025-03-31_16-10): ")

# Define file paths for tagged payloads and results
tagged_file = os.path.join(folder, "payloads_tagged.csv")
results_file = os.path.join(folder, "results.csv")
readme_file = os.path.join(folder, "README.md")

# Check if the tagged payload file exists
if not os.path.exists(tagged_file):
    print("❌ Tagged payloads file not found.")
    exit()

# Determine the number of payloads tested:
if os.path.exists(results_file):
    with open(results_file) as f:
        # Subtract one for the header row
        payload_count = sum(1 for _ in f) - 1
else:
    # If results file not found, use the count from tagged payloads
    with open(tagged_file) as f:
        reader = csv.DictReader(f)
        payload_count = sum(1 for _ in reader)

# Build risk summary from tagged payloads
risk = Counter()
with open(tagged_file) as f:
    reader = csv.DictReader(f)
    for row in reader:
        tag = row.get("tag", "").lower()
        for level in ["high", "medium", "low"]:
            if level in tag:
                risk[level] += 1

# Extract project name and timestamp from folder path
parts = folder.split("/")
project_name = parts[1] if len(parts) > 1 else "unknown"
timestamp = parts[-1]

# Build Markdown content for README.md
readme_content = f"""# Project Risk Report

**Project:** {project_name}  
**Scan Time:** {timestamp}  
**Payloads Tested:** {payload_count}

## Risk Summary

| Risk Level | Count |
|------------|-------|
| High       | {risk['high']} |
| Medium     | {risk['medium']} |
| Low        | {risk['low']} |

_This README was automatically generated based on the tagged payloads and test results._
"""

# Print the report (optional)
print(readme_content)

# Save the Markdown report to README.md
with open(readme_file, "w") as f:
    f.write(readme_content)

print(f"[✓] README.md generated at: {readme_file}")
