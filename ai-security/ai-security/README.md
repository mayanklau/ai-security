
# ⚔️ VulnScout – Agentic AI Security Toolkit

![VulnScout Logo](https://github.com/mayanklau/ai-security/raw/main/assets/banner.png)

> **VulnScout** is your AI-powered, agentic security companion — combining automation with essential open-source tools to help ethical hackers, researchers, and security teams rapidly identify and respond to web security threats.

---

## 🚀 Features at a Glance

| Tool      | Purpose                               |
|-----------|----------------------------------------|
| **Nmap**  | Network scanning & host discovery     |
| **SQLMap**| Automated SQL injection detection     |
| **WhatWeb**| Web technology fingerprinting         |
| **XSStrike**| AI-powered XSS vulnerability scanner |
| **Wfuzz** | Fuzzing for parameters/endpoints      |
| **Dirb**  | Directory brute-forcing               |
| **Nikto** | Web server vulnerability scanner      |
| **Amass** | Subdomain enumeration                 |

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/mayanklau/ai-security.git
cd ai-security

# Create a virtual environment
python3 -m venv ai-security-env
source ai-security-env/bin/activate

# Install dependencies
pip install -r requirements.txt


---

🧠 Usage

Run the interactive menu to execute any tool or all in one go:

python3 security_toolkit_menu.py

You can also run individual components like:

python3 main.py


---

📂 Project Structure

ai-security/
├── agents/                # Autonomous agents for scanning
├── modules/               # Core modules: tagging, testing, payloads
├── output/                # Results (JSON/CSV)
├── assets/                # Logo, images
├── security_toolkit_menu.py
└── main.py


---

🧩 Integrations & Capabilities

GPT tagging of payloads using OpenAI

Modular support for new tools

Result export in Markdown, JSON, and CSV

GitHub push and Telegram alert support



---

📜 License

Licensed under the MIT License.


---

> Created by Mayank Lau
Contribute, fork, and star the repo to support the project!



