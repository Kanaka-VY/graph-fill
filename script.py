import os
import random
from datetime import datetime, timedelta

# FIXED start date (your GitHub join date)
start_date = datetime(2025, 3, 12)
end_date = datetime.now()

current_date = start_date

while current_date <= end_date:

    # create small gaps
    if random.random() < 0.2:
        current_date += timedelta(days=1)
        continue

    commits = random.randint(2, 6)

    for j in range(commits):
        with open("file.txt", "a") as f:
            f.write(f"{current_date} commit {j}\n")

        os.system("git add .")
        os.system(
            f'git commit --date="{current_date.strftime("%Y-%m-%d %H:%M:%S")}" -m "backfill"'
        )

    current_date += timedelta(days=1)