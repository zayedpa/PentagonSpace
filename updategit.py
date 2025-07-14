import os
import subprocess
from datetime import datetime

REPO_PATH = r"C:\Desktop\PentagonSpace"

os.chdir(REPO_PATH)

# Generate commit message with current timestamp
commit_message = f"Auto commit on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("Git repository updated successfully!")
except subprocess.CalledProcessError as e:
    print("Error running Git commands:", e)
