# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "things-py>=1.0.1",
# ]
# ///

from collections import defaultdict

import things

task = things.completed(type="to-do", last="1w")

grouped = defaultdict(list)

for t in task:
    if t.get("stop_date"):
        day = t["stop_date"].split()[0]
        grouped[day].append(t["title"])

print("Last week's tasks:\n")
for day in sorted(grouped):
    print(day)
    for title in grouped[day]:
        print(f"- {title}")
    print()
