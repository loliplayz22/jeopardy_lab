from user import welcome_user, register_users, save_users_to_json, load_users_from_json
from trivia import load_trivia, choose_level_category, play_round
from leaderboard import build_leaderboard, print_leaderboard


def main():
    # Say hi and give the option to quit
    if not welcome_user():
        print("Goodbye!")
        return

    # Display trivia questions and set up players
    trivia_data = load_trivia()
    users = register_users()
    print("First user type:", type(users[0]).__name__)
    if not users:
        print("No players joined. Exiting.")
        return

    # Main game loop
    while True:
        level, category = choose_level_category(trivia_data)
        if not level or not category:
            print("Missing level or category. Exiting.")
            return

        # Each player takes a turn
        for user in users:
            play_round(user, trivia_data, level, category)

        # Save round results
        save_users_to_json(users, level=level, category=category)

        # Show leaderboards in different views
        all_rows = load_users_from_json()

        overall = build_leaderboard(all_rows)
        print_leaderboard(overall, "All-Time — All Categories")

        by_category = build_leaderboard(all_rows, category=category)
        print_leaderboard(by_category, f"All-Time — {category}")

        by_level_category = build_leaderboard(all_rows, level=level, category=category)
        print_leaderboard(by_level_category, f"All-Time — {level.capitalize()} {category}")

        # Ask if the players want to keep going
        again = input("\nPlay another round? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            break


if __name__ == "__main__":
    main()
