import os

while True:
    print("\n==== AI SECURITY TOOLKIT ====")
    print("1. Run Full Scan (All Tools)")
    print("2. View Reports")
    print("3. Push Latest Report to GitHub")
    print("4. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        os.system("python ~/ai-security/reports/tool_runner.py")
    elif choice == "2":
        os.system("ls -lt ~/ai-security/reports | head -n 10")
    elif choice == "3":
        os.system("bash ~/ai-security/push_report.sh")
    elif choice == "4":
        break
    else:
        print("Invalid choice. Try again.")
