import os
import random
from datetime import datetime, timedelta

start_date = datetime.now() - timedelta(days=60)

for i in range(60):
    date = start_date + timedelta(days=i)
    commits = random.randint(2, 6)

    for j in range(commits):
        with open("file.txt", "a") as f:
            f.write(f"{date} commit {j}\n")

        os.system("git add .")
        os.system(f'git commit --date="{date.strftime("%Y-%m-%d %H:%M:%S")}" -m "commit"')