import time
import subprocess
from datetime import datetime

# Change this value to set time gap (in seconds)
SLEEP_INTERVAL = 3 * 60 * 60  # 3 hours

def log(msg):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{now}] {msg}"
    print(line)
    with open("output/background_log.txt", "a") as f:
        f.write(line + "\n")

while True:
    log("Running Agentic Scanner...")
    try:
        subprocess.run(["python", "main.py"], check=True)
    except Exception as e:
        log(f"Error running main.py: {e}")
    
    log(f"Sleeping for {SLEEP_INTERVAL / 60:.0f} minutes...\n")
    time.sleep(SLEEP_INTERVAL)

