import os

# Function to run Nmap
def run_nmap():
    print("Running Nmap scan...")
    os.system("nmap -sP 192.168.0.1/24")  # Replace with your actual Nmap command
    print("Nmap scan complete!")

# Function to run SQLMap
def run_sqlmap():
    print("Running SQLMap scan...")
    os.system("sqlmap -u http://example.com --batch")  # Replace with your actual SQLMap command
    print("SQLMap scan complete!")

# Function to run WhatWeb
def run_whatweb():
    print("Running WhatWeb scan...")
    os.system("whatweb http://example.com")  # Replace with your actual WhatWeb command
    print("WhatWeb scan complete!")

# Function to run XSStrike
def run_xsstrike():
    print("Running XSStrike scan...")
    os.system("xsstrike -u http://example.com")  # Replace with your actual XSStrike command
    print("XSStrike scan complete!")

# Function to run Wfuzz
def run_wfuzz():
    print("Running Wfuzz scan...")
    os.system("wfuzz -c -z file,/path/to/wordlist -u http://example.com/FUZZ")  # Replace with your actual Wfuzz command
    print("Wfuzz scan complete!")

# Function to run Dirb
def run_dirb():
    print("Running Dirb scan...")
    os.system("dirb http://example.com")  # Replace with your actual Dirb command
    print("Dirb scan complete!")

# Function to run Nikto
def run_nikto():
    print("Running Nikto scan...")
    os.system("nikto -h http://example.com")  # Replace with your actual Nikto command
    print("Nikto scan complete!")

# Function to run Amass
def run_amass():
    print("Running Amass scan...")
    os.system("amass enum -d example.com")  # Replace with your actual Amass command
    print("Amass scan complete!")

# Menu function
def show_menu():
    print("\n==== AI Security Toolkit ====")
    print("1. Run Nmap Scan")
    print("2. Run SQLMap Scan")
    print("3. Run WhatWeb Scan")
    print("4. Run XSStrike Scan")
    print("5. Run Wfuzz Scan")
    print("6. Run Dirb Scan")
    print("7. Run Nikto Scan")
    print("8. Run Amass Scan")
    print("9. Exit")

# Main function
def main():
    while True:
        show_menu()
        choice = input("Select an option (1-9): ")

        if choice == "1":
            run_nmap()
        elif choice == "2":
            run_sqlmap()
        elif choice == "3":
            run_whatweb()
        elif choice == "4":
            run_xsstrike()
        elif choice == "5":
            run_wfuzz()
        elif choice == "6":
            run_dirb()
        elif choice == "7":
            run_nikto()
        elif choice == "8":
            run_amass()
        elif choice == "9":
            print("Exiting the toolkit.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the menu-driven program
if __name__ == "__main__":
    main()
