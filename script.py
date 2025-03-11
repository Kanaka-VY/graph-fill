import os
import random
from datetime import datetime, timedelta

# Your GitHub join date
start_date = datetime(2025, 3, 12)
end_date = datetime.now()

current_date = start_date

while current_date <= end_date:

    # Create gaps (skip some days)
    if random.random() < 0.25:  # 25% chance to skip day
        current_date += timedelta(days=1)
        continue

    # Random commits per active day
    commits = random.randint(2, 6)

    for j in range(commits):
        with open("file.txt", "a") as f:
            f.write(f"{current_date} commit {j}\n")

        os.system("git add .")
        os.system(
            f'git commit --date="{current_date.strftime("%Y-%m-%d %H:%M:%S")}" -m "activity"'
        )

    current_date += timedelta(days=1)