import os, json, random

# Loads in questions from trivia_data.json

trivia_data_path = os.path.join(os.path.dirname(__file__), "..", "data", "trivia_data.json")



def load_trivia():

    print("Loading trivia from:", os.path.abspath(trivia_data_path))

    try:

        with open(trivia_data_path, "r", encoding="utf-8") as f:

            data = json.load(f)

        print("Top-level keys:", list(data.keys()))

        return data

    except FileNotFoundError:

        print("Error: trivia_data.json not found.")

        return {}

    except json.JSONDecodeError as e:

        print("Error: trivia_data.json has invalid JSON.", e)

        return {}



# User choose difficulty level

def choose_from_list(prompt_text, items):

    """Show a numbered list and return the selected item."""

    if not items:

        return ""

    while True:

        print(f"\n{prompt_text}")

        for i, item in enumerate(items, start=1):

            print(f"{i}. {item}")

        s = input("Pick a number: ").strip()

        if s.isdigit():

            n = int(s)

            if 1 <= n <= len(items):

                return items[n - 1]

        print("Invalid choice. Try again.")



def choose_level_category(trivia_data):

    levels = list(trivia_data.keys())

    level = choose_from_list("Choose a level:", levels)

    if not level:

        return "", ""



    categories = list(trivia_data.get(level, {}).keys())

    print("Categories for that level:", categories)

    category = choose_from_list("Choose a category:", categories)

    if not category:

        return "", ""



    return level, category  





def ask_questions(questions, number_to_ask=5):

    correct_count = 0

    total_to_ask = min(number_to_ask, len(questions))

    selected = random.sample(questions, k=total_to_ask)



    for qnum, q in enumerate(selected, start=1):

        print(f"\nQ{qnum}: {q['q']}")

        for idx, text in enumerate(q["options"], start=1):

            print(f"{idx}. {text}")



        ans = input("Your answer (1-4): ").strip()

        if ans.isdigit():

            n = int(ans)

            if 1 <= n <= 4:

                if (n - 1) == q["answer"]:

                    print("Correct!")

                    correct_count += 1

                else:

                    print(f"Wrong! Correct answer: {q['options'][q['answer']]}")

            else:

                print("Invalid number. Counting as wrong.")

        else:

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

    """Run one player's turn and add points to user.points."""

    print(f"\n--- {user.full_name()}'s turn ---")



    questions = trivia_data.get(level, {}).get(category, [])

    if not questions:

        print("No questions available in this level/category.")

        return



    got = ask_questions(questions, number_to_ask=5)

    mult = level_multiplier(level)

    gained = got * mult

    user.points += gained



    print(f"{user.full_name()} got {got} correct on {level} (x{mult}). "

          f"Gained {gained}. Total = {user.points}")

    

    if user.kids_name: 

        print(f"{user.kids_name} is proud of you, {user.first_name}!")
