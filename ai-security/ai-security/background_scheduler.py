import time
import subprocess
from datetime import datetime

# Set the scan interval in seconds.
# For example, 6 hours = 21600 seconds.
# Adjust SCAN_INTERVAL as needed.
SCAN_INTERVAL = 21600  # 6 hours

while True:
    # Get the current time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] Starting scheduled scan...")

    # Run the full scan using agent.py
    # Replace the URL with your target if needed.
    subprocess.run(["python", "agent.py", "scan", "--url", "http://demo.testfire.net"], check=True)

    # Log completion time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] Scan complete. Waiting for next run...")

    # Sleep until the next scheduled scan
    time.sleep(SCAN_INTERVAL)
