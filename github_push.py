import os
import subprocess

folder = input("Enter full folder path to push (e.g. projects/demo.testfire.net/2024-04-01_19-42): ")

if not os.path.exists(folder):
    print("❌ Folder not found.")
    exit()

# Stage all files inside that folder
os.system(f"git add {folder}")

# Commit with timestamp message
commit_message = f"Auto-push for {folder}"
os.system(f"git commit -m \"{commit_message}\"")

# Push to GitHub
try:
    subprocess.run(["git", "push"], check=True)
    print(f"[✓] Successfully pushed {folder} to GitHub.")
except subprocess.CalledProcessError:
    print("❌ GitHub push failed. Check remote setup or internet connection.")
