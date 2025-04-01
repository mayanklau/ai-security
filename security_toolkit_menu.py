import os

# Function to run Nmap
def run_nmap():
    print("Running Nmap scan...")
    os.system("nmap -sP 192.168.0.1/24")  # Nmap scan
    print("Nmap scan complete!")

# Function to run SQLMap
def run_sqlmap():
    print("Running SQLMap scan...")
    os.system("python3 ./sqlmap/sqlmap.py -u http://example.com --batch")  # Path to SQLMap
    print("SQLMap scan complete!")

# Function to run WhatWeb
def run_whatweb():
    print("Running WhatWeb scan...")
    os.system("ruby ./WhatWeb/whatweb http://example.com")  # Path to WhatWeb
    print("WhatWeb scan complete!")

# Function to run XSStrike
def run_xsstrike():
    print("Running XSStrike scan...")
    os.system("python3 ./XSStrike/xsstrike.py -u http://example.com")  # Path to XSStrike
    print("XSStrike scan complete!")

# Function to run Wfuzz
def run_wfuzz():
    print("Running Wfuzz scan...")
    os.system("python3 ./wfuzz/wfuzz.py -c -z file,/path/to/wordlist -u http://example.com/FUZZ")  # Path to Wfuzz
    print("Wfuzz scan complete!")

# Function to run Dirb
def run_dirb():
    print("Running Dirb scan...")
    os.system("dirb http://example.com")  # Dirb is globally accessible
    print("Dirb scan complete!")

# Function to run Nikto
def run_nikto():
    print("Running Nikto scan...")
    os.system("perl ./nikto/nikto.pl -version")  # Path to Nikto
    print("Nikto scan complete!")

# Function to run Amass
def run_amass():
    print("Running Amass scan...")
    os.system("amass enum -d example.com")  # Path to Amass
    print("Amass scan complete!")

# Function to run all tools in sequence
def run_all_tools():
    run_nmap()
    run_sqlmap()
    run_whatweb()
    run_xsstrike()
    run_wfuzz()
    run_dirb()
    run_nikto()
    run_amass()

# Main function
def main():
    print("Starting all tools...")
    run_all_tools()
    print("All tools have been executed.")

# Run the main function
if __name__ == "__main__":
    main()
