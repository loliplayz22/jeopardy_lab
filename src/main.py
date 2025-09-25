from user import welcome_user, register_users, save_users_to_json, load_users_from_json
from trivia import load_trivia, choose_level_category, play_round
from leaderboard import build_leaderboard, print_leaderboard


def main():
    if not welcome_user():
        print("To bad you're not joining us!")
        return

    # Set up trivia questions and players
    trivia_data = load_trivia()
    if not trivia_data:
        print ("Trivia data not loaded. Check files.")
    users = register_users()
    if not users:
        print ("No players joined. Program quitting...")
    print("First user type:", type(users[0]).__name__)
    if not users:
        print("No players joined. Exiting.")
        return

    while True:
        level, category = choose_level_category(trivia_data)
        if not level or not category:
            print("Missing level or category. Exiting.")
            return
        # Save results of users
        for user in users:
            play_round(user, trivia_data, level, category)

        save_users_to_json(users, level=level, category=category)

        
        all_rows = load_users_from_json()

        overall = build_leaderboard(all_rows)
        print_leaderboard(overall, "All-Time — All Categories")

        by_category = build_leaderboard(all_rows, category=category)
        print_leaderboard(by_category, f"All-Time — {category}")

        by_level_category = build_leaderboard(all_rows, level=level, category=category)
        print_leaderboard(by_level_category, f"All-Time — {level.capitalize()} {category}")

        again = input("\nPlay another round? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            break

if __name__ == "__main__":
    main()
