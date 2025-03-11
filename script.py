import os
import random
from datetime import datetime, timedelta

start_date = datetime(2025, 3, 12)
end_date = datetime(2025, 5, 1)  # focus early months

current_date = start_date

while current_date <= end_date:

    commits = random.randint(8, 15)  # strong commits

    for j in range(commits):
        with open("file.txt", "a") as f:
            f.write(f"{current_date} fix\n")

        os.system("git add .")
        os.system(
            f'git commit --date="{current_date.strftime("%Y-%m-%d %H:%M:%S")}" -m "fix early graph"'
        )

    current_date += timedelta(days=1)