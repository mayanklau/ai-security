import sys, os, csv
from datetime import datetime
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.payloads.generator import generate_all
from modules.tagging.gpt_tagger import tag_payloads

folder = input("Enter target name (e.g. demo.testfire.net): ")
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
project_path = os.path.join("projects", folder, timestamp)
os.makedirs(project_path, exist_ok=True)

payloads = generate_all()
tagged = tag_payloads(payloads[:100])

with open(os.path.join(project_path, "payloads_tagged.csv"), "w") as f:
    writer = csv.DictWriter(f, fieldnames=["payload", "tag", "time"])
    writer.writeheader()
    writer.writerows(tagged)

print(f"[✓] Tagged payloads saved to: {project_path}/payloads_tagged.csv")
