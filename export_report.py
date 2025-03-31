import os
from datetime import datetime

# Sample scan result (replace with real data later)
scan_summary = {
    "target": "https://example.com",
    "vulnerabilities": [
        {"type": "XSS", "payload": "<script>alert(1)</script>", "status": "Reflected"},
        {"type": "SQLi", "payload": "' OR '1'='1", "status": "Not vulnerable"}
    ]
}

# Create timestamped filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"report_{timestamp}.md"

# Write Markdown report
with open(filename, "w") as f:
    f.write(f"# AI Security Scan Report\n")
    f.write(f"**Target**: {scan_summary['target']}\n\n")
    f.write("## Vulnerabilities Found:\n")
    for v in scan_summary["vulnerabilities"]:
        f.write(f"- **{v['type']}**\n")
        f.write(f"  - Payload: `{v['payload']}`\n")
        f.write(f"  - Status: {v['status']}\n\n")

print(f"[+] Report saved as: {filename}")
