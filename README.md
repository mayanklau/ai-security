VulnScout – Scouting for vulnerabilities in your web applications.

Agentic Security Toolkit

The Agentic Security Toolkit is a comprehensive, script-driven utility designed to help learners, researchers, and ethical hackers generate, test, and analyze common web-based attack payloads. It helps simulate how injection payloads interact with target web applications and generates detailed risk reports. The toolkit also integrates GitHub for easy versioning, sharing, and pushing results to remote repositories.

This tool is specifically built for educational and ethical hacking purposes, allowing users to perform penetration testing, CTF challenges, and security analysis on websites. The functionality is modular, allowing users to easily extend or integrate it into their existing security toolchain.


---

Features

Payload Generator

Generates a comprehensive set of payloads across:

Cross-Site Scripting (XSS)

SQL Injection (SQLi)

Local File Inclusion (LFI)

Remote Command Execution (RCE)



Payload Tester

Automatically sends generated payloads to a specified target URL and checks for signs of reflection or exposure. It provides basic testing for vulnerabilities like XSS, SQLi, and RCE.


Risk Report Generation

Generates a detailed risk report in Markdown format summarizing the results of the scan. The report includes risk levels for each payload and an overview of the scan results.


Exportable Results

Stores all payloads and findings in structured text, CSV, or JSON formats for easy review, reporting, and extension.


Secure Key Management

Reads configuration and API keys securely via a .env file using python-dotenv. This ensures that no sensitive data is hardcoded into the scripts.


GitHub Integration

Pushes scan results and payload data to a GitHub repository for versioning, backup, and sharing. The github_push.py script automates this process.


Modular Design

The toolkit consists of simple Python scripts (e.g., generate_payloads.py, test_payloads.py) that are easy to extend or integrate into larger tools or pipelines.


Background Scheduling

Automatically runs scans on a scheduled basis using the background_scheduler.py script. You can set a custom scan interval (e.g., every 6 hours) without requiring manual intervention.


Manual Tagging

Allows manual tagging of payloads based on user input. Users can tag payloads as "XSS", "SQLi", "RCE", or "Unknown" and the tags will be saved and reported.


Logs and Reports

Generates logs and detailed reports in CSV and JSON formats, which are essential for auditing, reviewing, and tracking test results.



---

Use Cases

Quick testing of web input fields and reflection behavior.

Cybersecurity education and experimentation.

CTF challenge development.

Penetration testing payload generation starter kit.

Regular scheduled scans with automated risk reporting.

GitHub integration for version control of scan data and reports.



---

Structure

├── generate_payloads.py        # Creates categorized attack payloads
├── test_payloads.py            # Sends payloads to target and logs reflections
├── generate_report.py          # Generates a risk report in Markdown format
├── github_push.py              # Pushes data to GitHub
├── background_scheduler.py     # Runs scans automatically on a schedule
├── payloads.txt                # Stores generated payloads
├── results.txt                 # Stores test findings in plain text format
├── results.csv                 # Stores test findings in CSV format
├── results.json                # Stores test findings in JSON format
├── .env                        # Secure local configuration (not tracked by Git)
├── README.md                   # This documentation
├── projects/                   # Stores project-specific folders and scan results
└── queue/                      # Contains queued scanning jobs for background processing


---

Getting Started

1. Install Dependencies:

Install the required dependencies using pip:

pip install -r requirements.txt

2. Configure the .env File:

Add your target URL and API keys (if applicable) to the .env file. Example:

TARGET_URL=http://example.com
OPENAI_API_KEY=your_openai_api_key

3. Run the Toolkit:

Generate Payloads:

python generate_payloads.py

Test Payloads:

python test_payloads.py

Generate the Risk Report:

python generate_report.py

Automatically Push Results to GitHub:

python github_push.py

Schedule Scans Automatically:

Run the scheduled scan script (configurable interval):

python background_scheduler.py

Tag Payloads Manually:

If you want to tag payloads manually, use the following:

python manual_tagging.py


---

Additional Functionality

Running in Background: If you want scans to run automatically at regular intervals, you can use the background scheduler to trigger scans periodically.

Logs and Results Export: All results from tests are saved in the results.txt, results.csv, and results.json files. These can be easily shared or stored for later reference.



---

Disclaimer

This tool is intended for educational and ethical testing purposes only. Use it only on systems you own or have explicit permission to test. Unauthorized access to computer systems is illegal.


