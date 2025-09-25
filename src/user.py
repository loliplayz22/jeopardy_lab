import json
user_data_path = "../data/user_data.json"

# Create User Class
class User:
    def __init__ (self, first_name, last_name, kids_name):
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.kids_name = kids_name.strip()
        self.points = 0
    
    def full_name (self):
        return f"{self.first_name} {self.last_name}"
    
    def save_user_to_dictonary (self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "kids_name": self.kids_name, 
            "points": self.points
        }
    
# Welcome user to the game
def welcome_user ():
    print ("———Welcome to the Trivia Game!———–")
    while True:
        ans = input ("Are you ready for Trivia? (y/n) ").strip().lower()
        if ans in ("y", "yes"):
            return True
        elif ans in ("n", "non"):
            return False
        else:
            print ("Please type yes or no.")

# Collecting all the players
#def register_users():
    users = []
    print ("Enter your information as a player. When you're finished adding players, type 'Done' for fist name. ")
    while True:
        first_name = input ("First name: ").strip()
        if first_name.lower() == "done":
            break
        last_name = input ("Last name: ")
        kids = input ("Kids name: ")
        print (f"{first_name} {last_name}, welcome to Trivia!")
    return users

def register_users():
    users = []
    print("\nEnter player info. Type 'done' for first name to stop adding players.")
    while True:
        first_name = input("First name: ").strip()
        if first_name.lower() == "done":
            break
        last_name = input("Last name: ").strip()
        kids_name = input("Kids name (optional): ").strip()
        users.append(User(first_name, last_name, kids_name))
        new_user = User(first_name, last_name, kids_name)
        users.append(new_user)
        print(f"{first_name} {last_name}, welcome to Trivia!\n")
    return users 

# Save user data to user_data.json
def save_users_to_json():
    try: 
        with open (user_data_path, "r", encoding="utf-8") as f: 
            return json.load(f)
    except (FileNotFoundError, json.jsonDecodeError):
        rows = []

    for i in users:
        row = i.dict()
        row ["level"] = level
        row ["category"] = category or ""
        row.append(row)
# Write back the user data from user_data.json
    with open (user_data_path, "r", encoding = "utf-8")as f: 
        return json.dump(rows, f, indent=3)

# Loads all the rows of user_data.json as a dictionary
def load_users_from_json():
    try: 
         with open (user_data_path, "r", encoding="utf-8") as f: 
            return json.load(f)
    except(FileNotFoundError, json.jsonDecodeError):
        return []
