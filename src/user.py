import os, json

# Create the data path of user, using os
user_data_path = os.path.join(
    os.path.dirname(__file__),  
    "..",                       
    "data",
    "user_data.json"
)

# Create the User class
class User:
    def __init__(self, first_name, last_name, kids_name):
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.kids_name = kids_name.strip()
        self.points = 0  

    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    def save_user_to_dictonary(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "kids_name": self.kids_name,
            "points": self.points
        }

# Display function to welcome user to game
def welcome_user():
    print("=== Welcome to the Trivia Game! ===")
    while True:
        ans = input("Are you ready for Trivia? (y/n) ").strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Please type yes or no.")

def register_users():
    """Ask for players until the user types 'done' for first name."""
    users = []
    print("\nEnter player info. Type 'done' for first name to stop adding players.")
    while True:
        first_name = input("First name: ").strip()
        if first_name.lower() == "done":
            break
        last_name = input("Last name: ").strip()
        kids_name = input("Kids name (optional): ").strip()

        new_user = User(first_name, last_name, kids_name)
        users.append(new_user)
        print(f"{new_user.full_name()}, welcome to Trivia!\n")

    return users

# Save user data to user_data.json
def save_users_to_json(users, level=None, category=None):
    try:
        with open(user_data_path, "r", encoding="utf-8") as f:
            rows = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        rows = []

    for i in users:
        row = i.save_user_to_dictonary()
        row["level"] = level or ""
        row["category"] = category or ""
        rows.append(row)

    os.makedirs(os.path.dirname(user_data_path), exist_ok=True)
    with open(user_data_path, "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=3)

def load_users_from_json():
    try:
        with open(user_data_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
