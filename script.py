import os
import random
from datetime import datetime

date = datetime.now()

# random commits for today
commits = random.randint(3, 10)

for j in range(commits):
    with open("file.txt", "a") as f:
        f.write(f"{date} commit {j}\n")

    os.system("git add .")
    os.system(
        f'git commit --date="{date.strftime("%Y-%m-%d %H:%M:%S")}" -m "daily commit"'
    )

# push automatically
os.system("git push origin main")