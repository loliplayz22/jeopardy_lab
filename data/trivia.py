import json
import random
from user import User

TRIVIA_DATA_PATH = "../datba/trivia_data.json"


def load_trivia():
    try:
        with open(TRIVIA_DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error: trivia_data.json is missing or invalid.")
        return {}


def choose_from_list(prompt_text, choices):
    """
    Show a numbered list and return the selected item (string).
    Keeps asking until a valid number is entered.
    """
    if not choices:
        return ""
    while True:
        print(f"\n{prompt_text}")
        for index, item in enumerate(choices, start=1):
            print(f"{index}. {item}")
        pick = input("Pick a number: ").strip()
        if pick.isdigit():
            i = int(pick) - 1
            if 0 <= i < len(choices):
                return choices[i]
        print("Invalid choice. Try again.")


def choose_level_category(trivia_data):
    levels = list(trivia_data.keys())
    level = choose_from_list("Choose a level:", levels)
    categories = list(trivia_data.get(level, {}).keys())
    category = choose_from_list("Choose a category:", categories)
    return level, category


def ask_questions(questions, number_to_ask=5):
    """
    Ask up to number_to_ask random questions.
    Return how many were answered correctly (integer).
    """
    correct_count = 0
    # Random non-repeating selection
    selected = random.sample(questions, k=min(number_to_ask, len(questions)))

    for q_index, q in enumerate(selected, start=1):
        print(f"\nQ{q_index}: {q['q']}")
        for opt_index, option in enumerate(q["options"], start=1):
            print(f"{opt_index}. {option}")

        answer_text = input("Your answer (1-4): ").strip()

        if answer_text.isdigit():
            chosen = int(answer_text)
            if 1 <= chosen <= len(q["options"]):
                if chosen - 1 == q["answer"]:
                    print("Correct!")
                    correct_count += 1
                else:
                    correct_option = q["options"][q["answer"]]
                    print(f"Wrong! Correct: {correct_option}")
                continue

        # If we reach here, input was invalid
        print("Invalid input. Counting as wrong.")
    return correct_count


def level_multiplier(level):
    if level == "easy":
        return 1
    elif level == "medium":
        return 2
    elif level == "hard":
        return 3
    else:
        return 1


def play_round(user, trivia_data, level, category):
    """
    One user's turn:
    - Ask 5 questions from level+category
    - Multiply by difficulty
    - Add to user.points
    """
    print(f"\n--- {user.full_name()}'s turn ---")
    questions = trivia_data.get(level, {}).get(category, [])
    if not questions:
        print("No questions available in this level/category.")
        return

    correct_in_round = ask_questions(questions, number_to_ask=5)
    multiplier = level_multiplier(level)
    gained_points = correct_in_round * multiplier

    user.points += gained_points
    print(
        f"{user.full_name()} got {correct_in_round} correct on {level} "
        f"(x{multiplier}). Gained {gained_points}. Total = {user.points}"
    )
