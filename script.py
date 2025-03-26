import os
import random
from datetime import datetime, timedelta

start_date = datetime.now() - timedelta(days=365)

for i in range(365):
    date = start_date + timedelta(days=i)

    commits = random.randint(3, 8)

    for j in range(commits):
        with open("file.txt", "a") as f:
            f.write(f"{date} commit {j}\n")

        os.system("git add .")
        os.system(
            f'git commit --date="{date.strftime("%Y-%m-%d %H:%M:%S")}" -m "backfill"'
        )