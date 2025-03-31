import os, time

queue_file = "queue.txt"

if not os.path.exists(queue_file):
    print("queue.txt not found. Create it and add one command per line.")
    exit()

with open(queue_file, "r") as f:
    lines = [line.strip() for line in f if line.strip()]

for cmd in lines:
    print(f"\n[•] Running: {cmd}")
    os.system(cmd)
    print("[✓] Done\n")
    time.sleep(2)  # Pause between jobs

# Clear queue after running
open(queue_file, "w").close()
print("[✓] Queue completed and cleared.")
