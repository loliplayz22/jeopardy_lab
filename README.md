###### TRIVIA (FAMILY-DAY) LAB
is a question-and-answer game built using Python and Flask. The goal of the project is to create an interactive game that challenges users with trivia questions, checks their answers, and keeps track of scores in a fun and easy-to-use format.

---

### 1. WHAT THE PROGRAM DOES

TRIVIA is a terminal or web-based application that:
- retrieves users and their names
- Loads trivia questions and answers from a structured JSON file
- Displays individual questions to users, one at a time
- Tracks the score of each player based on correct or incorrect responses
- Can serve multiple users (players) and keep track of each player’s score individually




### 2. All trivia content (questions, answers, categories, and point values) is stored in a separate JSON file. 

# Each question in the JSON file includes:
- A unique ID
- The category 
- The question text
- The correct answer
- A point value

## 3. Team Roles

# Person 1 (Kimberly): Responsible for trivia question data
- Creates and maintains data/trivia_data.json 
- Make sure the JSON format is correct and can be read easily

# Person 2 (Grace): Handles user setup in user.py and user_data.json
- Defines the user class and related functions in src/user.py
- Manages data/user_data.json, storing player information and scores
- Ensures users' data is inputted and stored correctly

# Person 3 (Loli): Handles trivia.py and running the actual game
- Implements game logic
- Works in src/trivia.py
- Handles how rounds are played, asking questions, and updating points.
- Connects trivia data and system so the game works smoothly

# Person 4 (Mia): Imports into main file and creates the leaderboard.py file 

- Brings the pieces together.
- Saves user data 
- Keeps track of high scores
- Writes the main program in src/main.py that imports all modules and runs the game.
- Creates src/leaderboard.py to sort and display scores.
- Makes sure everything is working and the leaderboard works

### 4. Project Structure

project/
  data/
    user_data.json      stores user profiles and scores
    trivia_data.json    stores trivia questions
  src/
    main.py             runs the game, calls functions
    user.py             user class (name, score, etc.)
    trivia.py           trivia logic (questions, answers, scoring)
    leaderboard.py      do last, read user_data.json and rank scores

### 5. Daily work flow

-kimberly

finished JSON file which contains three levels, two category of questions and set the input option as a, b, c, d. Tomorrow I will work with Loli to make sure that the JSON file can be successfully imported and incorporated with the program .py


