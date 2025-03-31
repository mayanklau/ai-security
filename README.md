# ⚔️ VulnScout – The Agentic Security Toolkit

**Scouting for vulnerabilities in your web applications. Powered by AI + Classic Security Tools.**  
A modular, script-driven toolkit for ethical hackers, researchers, and red teamers. Built for **Termux**, integrated with **GitHub**, and designed to be extended.

---

## 🚀 Features

### ✅ Agentic AI Modules
- **Payload Generator** for:
  - XSS
  - SQLi
  - LFI
  - RCE
- **Payload Tester**: Automatically tests target URL for reflected or injectable vulnerabilities.
- **Manual Tagging**: Tag payloads as XSS, SQLi, RCE, or Unknown.
- **Risk Report Generator**: Markdown-based reports with risk summaries.
- **Scheduler**: Run background scans every few hours (via `background_scheduler.py`).
- **GitHub Integration**: Push payloads, results, and reports to your repo automatically.
- **.env Config**: Secure config with OpenAI API key and target URL.

---

### 🔧 Integrated Security Tools
| Tool        | Purpose                  |
|-------------|---------------------------|
| `nmap`      | Network scanning          |
| `sqlmap`    | SQL Injection detection   |
| `whatweb`   | Web tech fingerprinting   |
| `xsstrike`  | AI-powered XSS scanner    |
| `wfuzz`     | Parameter fuzzing         |
| `dirb`      | Directory brute-force     |
| `nikto`     | Web vulnerability scanner |
| `amass`     | Subdomain enumeration     |

---

## 🗂️ Folder Structure

ai-security/ ├── menu.py                   # CLI launcher ├── push_report.sh            # GitHub push automation ├── reports/ │   ├── tool_runner.py        # Main scanner: Nmap, Sqlmap, XSStrike, etc. │   └── report_*.md           # Generated reports ├── generate_payloads.py      # Agentic payload generator ├── test_payloads.py          # Payload testing module ├── manual_tagging.py         # Optional payload labeler ├── generate_report.py        # Risk report creator ├── github_push.py            # GitHub sync script ├── background_scheduler.py   # Runs scans on intervals ├── .env                      # Secrets + config (excluded from Git) ├── output/ │   ├── payloads_tagged.csv/.json │   ├── results.csv/.json │   └── log.txt

---

## ⚙️ Getting Started

### 1. Install Requirements
```bash
pip install -r requirements.txt
pkg install git python curl nmap perl dirb -y

2. Setup .env file

TARGET_URL=http://example.com
OPENAI_API_KEY=sk-xxxxxxxxxxx

3. Run Core Modules

python generate_payloads.py
python test_payloads.py
python generate_report.py

4. Push to GitHub

python github_push.py

5. Schedule Background Scans

python background_scheduler.py


---

✨ Use Cases

Fast payload generation and testing for CTFs

Scheduled recon on authorized targets

Learn web security hands-on with integrated tools

Maintain a GitHub-based trail of risk findings

Automate red team prep via Termux



---

⚠️ Disclaimer

This tool is intended only for educational and authorized security testing.
Never scan or attack systems you don’t have permission to test.
Unauthorized access is illegal and unethical.


---

⭐ Credits

Created by @mayanklau — Powered by OpenAI + Termux + classic infosec tools.

