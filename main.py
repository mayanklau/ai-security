from modules.payloads.generator import generate_all
from modules.tagging.gpt_tagger import tag_payloads
from modules.testing.tester import test_payloads
from modules.utils.logger import log
import csv, json, os

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

# Step 1: Generate Payloads
payloads = generate_all()
log(f"Generated {len(payloads)} payloads")

# Step 2: Tag with GPT
log("Tagging first 100 payloads using GPT...")
tagged = tag_payloads(payloads[:100])

# Step 3: Save tagged payloads
with open("output/payloads_tagged.json", "w") as jf:
    json.dump(tagged, jf, indent=2)

with open("output/payloads_tagged.csv", "w") as cf:
    writer = csv.DictWriter(cf, fieldnames=["payload", "tag", "time"])
    writer.writeheader()
    writer.writerows(tagged)

log("Tagged payloads saved")

# Step 4: Get target URL
url = input("Enter target website URL (e.g. http://demo.testfire.net): ")

# Step 5: Test payloads on URL
log(f"Testing payloads against: {url}")
results = test_payloads(payloads[:100], url)

# Step 6: Save test results
with open("output/results.json", "w") as jf:
    json.dump(results, jf, indent=2)

with open("output/results.csv", "w") as cf:
    writer = csv.DictWriter(cf, fieldnames=["payload", "reflected", "error"])
    writer.writeheader()
    writer.writerows(results)

log("Testing results saved to output/")
