# TRIVIA (FAMILY-DAY) LAB

A question-and-answer game built using Python. The goal of the project is to create an interactive game that challenges users with trivia questions, checks their answers, and keeps track of scores in a fun and easy-to-use format.

---

## 1. What the Program Does

TRIVIA is a terminal program that:
- Retrieves users and their names
- Loads trivia questions and answers from a structured JSON file
- Displays individual questions to users, one at a time
- Tracks the score of each player based on correct or incorrect responses
- Can serve multiple users (players) and keep track of each player’s score individually

---

## 2. Trivia Content

All trivia content (questions, answers, categories, and point values) is stored in a separate JSON file.  
Each question in the JSON file includes:
- A unique ID
- The category 
- The question text
- The correct answer
- A point value

---

## 3. Team Roles

### Person 1 (Kimberly): Trivia Question Data
- Creates and maintains `data/trivia_data.json` 
- Ensures the JSON format is correct and can be read easily

### Person 2 (Grace): User Setup
- Defines the user class and related functions in `src/user.py`
- Manages `data/user_data.json` (player information and scores)
- Ensures user data is inputted and stored correctly

### Person 3 (Loli): Game Logic
- Implements game logic in `src/trivia.py`
- Handles rounds, questions, and scoring
- Connects trivia data with the system so the game works smoothly

### Person 4 (Mia): Integration and Leaderboard
- Brings all parts together in `src/main.py`
- Saves user data 
- Keeps track of high scores
- Creates `src/leaderboard.py` to sort and display scores

---

## 4. Project Structure

```
project/
  data/
    user_data.json      # stores user profiles and scores
    trivia_data.json    # stores trivia questions
  src/
    main.py             # runs the game, calls functions
    user.py             # user class (name, score, etc.)
    trivia.py           # trivia logic (questions, answers, scoring)
    leaderboard.py      # reads user_data.json and ranks scores
```


---

## 5. Daily Workflow

### Kimberly (Person 1)
- **09/24:** Finished JSON file with three levels (easy, medium, hard) and two categories (animals, science). Input options set as a, b, c, d.  
- **09/25:** Worked with Loli to ensure JSON file can be imported into `trivia.py`.

### Grace (Person 2)
- **09/24:** Completed all functions in the `User` class in `user.py`. Collaborated with teammates to run user functions in `main.py`.  
- **09/25:** Debugged `user.py` imports and integration.

### Loli (Person 3)
- **09/24:** Wrote the code for `trivia.py` and tested it with teammates.  
- **09/25:** Met with teammates.

### Mia (Person 4)
- **09/24:** Developed `main.py` to integrate all components and created `leaderboard.py` for rankings.  
- **09/25:** Debugged program with teammates.

