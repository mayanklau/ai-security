import os
import json

# Function to run Nmap (example command)
def run_nmap():
    print("Running Nmap scan...")
    os.system("nmap -sP 192.168.0.1/24")  # Replace with your actual Nmap command
    print("Nmap scan complete!")

# Function to run SQLMap (example command)
def run_sqlmap():
    print("Running SQLMap scan...")
    os.system("sqlmap -u http://example.com --batch")  # Replace with your actual SQLMap command
    print("SQLMap scan complete!")

# Function to run WhatWeb (example command)
def run_whatweb():
    print("Running WhatWeb scan...")
    os.system("whatweb http://example.com")  # Replace with your actual WhatWeb command
    print("WhatWeb scan complete!")

# Function to run XSStrike (example command)
def run_xsstrike():
    print("Running XSStrike scan...")
    os.system("xsstrike -u http://example.com")  # Replace with your actual XSStrike command
    print("XSStrike scan complete!")

# Function to run Wfuzz (example command)
def run_wfuzz():
    print("Running Wfuzz scan...")
    os.system("wfuzz -c -z file,/path/to/wordlist -u http://example.com/FUZZ")  # Replace with your actual Wfuzz command
    print("Wfuzz scan complete!")

# Function to run Dirb (example command)
def run_dirb():
    print("Running Dirb scan...")
    os.system("dirb http://example.com")  # Replace with your actual Dirb command
    print("Dirb scan complete!")

# Function to run Nikto (example command)
def run_nikto():
    print("Running Nikto scan...")
    os.system("nikto -h http://example.com")  # Replace with your actual Nikto command
    print("Nikto scan complete!")

# Function to run Amass (example command)
def run_amass():
    print("Running Amass scan...")
    os.system("amass enum -d example.com")  # Replace with your actual Amass command
    print("Amass scan complete!")

# Full Scan Logic
if __name__ == "__main__":
    # Run Nmap scan
    run_nmap()

    # Run SQLMap scan
    run_sqlmap()

    # Run WhatWeb scan
    run_whatweb()

    # Run XSStrike scan
    run_xsstrike()

    # Run Wfuzz scan
    run_wfuzz()

    # Run Dirb scan
    run_dirb()

    # Run Nikto scan
    run_nikto()

    # Run Amass scan
    run_amass()

    print("Full scan completed.")
