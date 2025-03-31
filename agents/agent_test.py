import sys, os, csv
from datetime import datetime
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.payloads.generator import generate_all
from modules.testing.tester import test_payloads

folder = input("Enter target name (e.g. demo.testfire.net): ")
url = input("Enter full URL (e.g. http://demo.testfire.net): ")
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
project_path = os.path.join("projects", folder, timestamp)
os.makedirs(project_path, exist_ok=True)

payloads = generate_all()
results = test_payloads(payloads[:100], url)

with open(os.path.join(project_path, "results.csv"), "w") as f:
    writer = csv.DictWriter(f, fieldnames=["payload", "reflected", "error"])
    writer.writeheader()
    writer.writerows(results)

print(f"[✓] Test results saved to: {project_path}/results.csv")
