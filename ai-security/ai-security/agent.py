import argparse
import os
import csv
import json
from datetime import datetime
from modules.payloads.generator import generate_all
from modules.tagging.gpt_tagger import tag_payloads
from modules.testing.tester import test_payloads
from modules.utils.logger import log

# CLI setup
parser = argparse.ArgumentParser(description="Agentic AI CLI")
subparsers = parser.add_subparsers(dest="command")

scan = subparsers.add_parser("scan")
scan.add_argument("--url", required=True)

tag_only = subparsers.add_parser("tag-only")

test_only = subparsers.add_parser("test-only")
test_only.add_argument("--url", required=True)

args = parser.parse_args()

# Project folder logic
if args.command in ["scan", "test-only"]:
    domain = args.url.replace("http://", "").replace("https://", "").replace("/", "_")
else:
    domain = "manual_tagging_" + datetime.now().strftime("%Y%m%d_%H%M%S")

project_folder = os.path.join("projects", domain)
os.makedirs(project_folder, exist_ok=True)

# Helpers to save results
def save_tagged(tagged, folder):
    with open(f"{folder}/payloads_tagged.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=["payload", "tag", "time"])
        writer.writeheader()
        writer.writerows(tagged)

def save_results(results, folder):
    with open(f"{folder}/results.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=["payload", "reflected", "error"])
        writer.writeheader()
        writer.writerows(results)

# Generate payloads
payloads = generate_all()

# Actions
if args.command == "scan":
    log(f"Running full scan for: {args.url}")
    tagged = tag_payloads(payloads[:100])
    save_tagged(tagged, project_folder)
    results = test_payloads(payloads[:100], args.url)
    save_results(results, project_folder)
    log("Scan complete.")

elif args.command == "tag-only":
    log("Tag-only mode...")
    tagged = tag_payloads(payloads[:100])
    save_tagged(tagged, project_folder)
    log("Tag-only complete.")

elif args.command == "test-only":
    log(f"Test-only for: {args.url}")
    results = test_payloads(payloads[:100], args.url)
    save_results(results, project_folder)
    log("Test-only complete.")

else:
    parser.print_help()
