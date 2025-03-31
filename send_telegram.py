import requests
import os

# Replace these with your actual Telegram Bot token and Chat ID
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

# Prompt for the project folder path (where risk_report.md is stored)
folder = input("Enter project folder path (e.g. projects/demo.testfire.net/2025-03-31_16-10): ")

# Define the risk report file path
report_file = os.path.join(folder, "risk_report.md")

# Check if the report file exists
if not os.path.exists(report_file):
    print("❌ risk_report.md not found in the specified folder!")
    exit()

# Read the report contents
with open(report_file, "r") as f:
    report = f.read()

# Prepare the URL for Telegram Bot API
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# Prepare the payload to send the message
payload = {
    "chat_id": CHAT_ID,
    "text": report
}

# Send the message via a POST request
response = requests.post(url, data=payload)

if response.status_code == 200:
    print("[✓] Telegram summary alert sent successfully!")
else:
    print("❌ Failed to send Telegram message.")
    print(response.text)
