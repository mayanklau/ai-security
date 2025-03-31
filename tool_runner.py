import os
import subprocess
from datetime import datetime

target = input("Enter target domain (e.g., example.com): ")
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
report_file = f"report_{timestamp}.md"

def run_command(label, cmd):
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True, timeout=90)
    except subprocess.CalledProcessError as e:
        output = e.output
    return f"## {label}\n```\n{output.strip()}\n```\n"

sections = []

sections.append(run_command("Nmap", f"nmap -T4 -F {target}"))
sections.append(run_command("SQLMap", f"python ~/sqlmap/sqlmap.py -u 'http://{target}/?id=1' --batch --level=1 --risk=1"))
sections.append(run_command("WhatWeb", f"perl ~/WhatWeb/whatweb {target}"))
sections.append(run_command("XSStrike", f"python3 ~/XSStrike/xsstrike.py --crawl --blind --url http://{target}/"))
sections.append(run_command("Wfuzz", f"wfuzz -u http://{target}/FUZZ -w /data/data/com.termux/files/usr/share/wordlists/dirb/common.txt --hc 404"))
sections.append(run_command("Dirb", f"dirb http://{target}"))
sections.append(run_command("Nikto", f"perl ~/nikto/program/nikto.pl -h http://{target}"))
sections.append(run_command("Amass", f"amass enum -d {target}"))

with open(report_file, "w") as f:
    f.write(f"# AI Security Toolkit Report\n\n")
    f.write(f"**Target**: {target}\n")
    f.write(f"**Timestamp**: {timestamp}\n\n")
    for section in sections:
        f.write(section + "\n")

print(f"[+] Report saved as {report_file}")
