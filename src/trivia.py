import os, json, random

TRIVIA_DATA_PATH = os.path.join(
    os.path.dirname(__file__),  # folder of trivia.py (src/)
    "..",                       # go up to project/
    "data",
    "trivia_data.json"
)

def load_trivia():
    # show exactly which file we try to open
    print("DEBUG: loading trivia from:", os.path.abspath(TRIVIA_DATA_PATH))
    try:
        with open(TRIVIA_DATA_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: trivia_data.json not found.")
        return {}
    except json.JSONDecodeError as e:
        print("Error: trivia_data.json has invalid JSON.", e)
        return {}

    # sanity check what we got
    print("DEBUG: top-level keys:", list(data.keys()))
    return data


def choose_from_list(prompt_text, choices):
    if not choices:
        return ""
    while True:
        print(f"\n{prompt_text}")
        for i, item in enumerate(choices, start=1):
            print(f"{i}. {item}")
        s = input("Pick a number: ").strip()
        if s.isdigit() and 1 <= int(s) <= len(choices):
            return choices[int(s) - 1]
        print("Invalid choice. Try again.")

def choose_level_category(trivia_data):
    # levels are the top-level keys
    levels = list(trivia_data.keys())
    print("DEBUG: levels for user to pick:", levels)
    level = choose_from_list("Choose a level:", levels)
    if not level:
        return "", ""

    # categories are inside the chosen level
    categories = list(trivia_data.get(level, {}).keys())
    print("DEBUG: categories for that level:", categories)
    category = choose_from_list("Choose a category:", categories)
    if not category:
        return "", ""
    print(f"\n--- {user.full_name()}'s turn ---")
    questions = trivia_data.get(level, {}).get(category, [])
    if not questions:
        print("No questions available in this level/category.")
        return

    correct_in_round = ask_questions(questions, number_to_ask=5)

    # difficulty multiplier
    if level == "easy":
        multiplier = 1
    elif level == "medium":
        multiplier = 2
    elif level == "hard":
        multiplier = 3
    else:
        multiplier = 1

    gained_points = correct_in_round * multiplier
    user.points += gained_points

    print(
