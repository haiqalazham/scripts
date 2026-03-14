#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "things-py>=1.0.1",
# ]
# ///

import sys
from collections import defaultdict

import things


def show_today():
    tasks = things.today()

    print("Today's tasks:\n")
    for t in tasks:
        print(f"- {t['title']}")


def show_last_week():
    tasks = things.completed(type="to-do", last="1w")

    grouped = defaultdict(list)

    for t in tasks:
        if t.get("stop_date"):
            day = t["stop_date"].split()[0]
            grouped[day].append(t["title"])

    print("Last week's tasks:\n")
    for day in sorted(grouped):
        print(day)
        for title in grouped[day]:
            print(f"- {title}")
        print()


def show_upcoming():
    tasks = things.upcoming()

    grouped = defaultdict(list)

    for t in tasks:
        if t.get("start_date"):
            day = t["start_date"].split()[0]
            grouped[day].append(t["title"])

    print("Upcoming tasks:\n")
    for day in sorted(grouped):
        print(day)
        for title in grouped[day]:
            print(f"- {title}")
        print()


def show_anytime():
    tasks = things.anytime()

    grouped = defaultdict(list)

    for t in tasks:
        if t.get("area_title"):
            area = t["area_title"]
            grouped[area].append(t["title"])

    print("Anytime tasks:\n")
    for area in sorted(grouped):
        print(area)
        for title in grouped[area]:
            print(f"- {title}")
        print()


def menu():
    print("Select an option:\n")
    print("1. Today's tasks")
    print("2. Upcoming tasks")
    print("3. Anytime tasks")
    print("4. Last week's completed tasks\n")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        print()
        show_today()
    elif choice == "2":
        print()
        show_upcoming()
    elif choice == "3":
        print()
        show_anytime()
    elif choice == "4":
        print()
        show_last_week()
    else:
        print("Invalid option")


def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()

        if arg in {"today", "t"}:
            show_today()
        elif arg in {"week", "w", "last-week"}:
            show_last_week()
        elif arg in {"upcoming"}:
            show_upcoming()
        elif arg in {"anytime"}:
            show_anytime()
        else:
            print("Unknown command")
    else:
        menu()


if __name__ == "__main__":
    main()
