# leaderboard.py

def build_leaderboard(rows, category=None, level=None):
    # filter rows
    filtered = []
    for row in rows:
        if category and row.get("category") != category:
            continue
        if level and row.get("level") != level:
            continue
        filtered.append(row)

    # total points by player
    totals = {}
    for row in filtered:
        name = (row.get("first_name", "") + " " + row.get("last_name", "")).strip()
        kids = row.get("kids_name", "")
        points = int(row.get("points", 0))

        if name in totals:
            totals[name]["points"] += points
        else:
            totals[name] = {"name": name, "kids_name": kids, "points": points}

    # order points high to low
    leaderboard = list(totals.values())
    leaderboard.sort(key=lambda x: x["points"], reverse=True)
    return leaderboard


def print_leaderboard(rows, title="Leaderboard"):
    if not rows:
        print(f"\nNo scores yet for {title}.")
        return

    print(f"\n=== {title} ===")
    print(f"{'Rank':<5}{'Name':<20}{'Kids':<12}{'Points':<6}")
    print("-" * 45)
    for i, row in enumerate(rows, start=1):
        kids = row["kids_name"] or "-"
        print(f"{i:<5}{row['name']:<20}{kids:<12}{row['points']:<6}")

