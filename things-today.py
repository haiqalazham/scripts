# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "things-py>=1.0.1",
# ]
# ///

import things

task = things.today()

print("Today's tasks:\n")
for t in task:
    print(f"- {t['title']}")
