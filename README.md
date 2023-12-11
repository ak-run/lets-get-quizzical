# Project Name

Short description or tagline of your project.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Run the App](#run-the-app)
- [Usage](#usage)
- [Testing](#testing)
- [Acknowledgments](#acknowledgments)

## Getting Started

### App structure
The app is divided into following directories: 
1. Project Root: it contains app.py to initialise the project, requirements.txt to install required Python packages and libraries, .gitignore with list of files and directories to be ignored by git.
2. static: it contains CSS stylesheet, JavaScript files, and images for the website.
3. templates: it contains HTML templates used by the app.
4. config: it contains config file for database connection (local as included by .gitignore) and an example config file with fake data to show the correct structure.
5. models: it contains main Python classes used in the app: DatabaseConnection, Leaderboard, QuizQuestions, and QuizGame.
6. routes: it contains route definitions for the application.
7. database: it contains files to create database needed for the leaderboard function of the app
8. tests: it contains unit tests (we used built Python framework - unittest)

### Prerequisites
#### Python packages
The app includes a number of standard python libraries that do not need installation. Those are imported in the files that use them.
The packages that need installation are in requirements.txt file:
- flask~=3.0.0 to run the app
- requests to make requests to external API with quiz questions
- mysql-connector-python for connection to the database
- Flask-WTF and wtforms for managing and validating data submitted through web forms

### Installation
To install the required packages for this project, follow these steps:
1. Open your command prompt or terminal.
2. Navigate to the project's directory using the `cd` command. For example:
```bash
cd /path-to-your-project
```
3. Run the following command to install the packages listed in the requirements.txt file:
```bash
pip install -r requirements.txt
```
This will install all the packages and their specified versions listed in the requirements.txt file, ensuring that you have the correct dependencies for the project.
#### SQL database
In database directory we added a file needed to add database to MySQL workbench. You can either:
- run [user_scores_init.sql](database%2Fuser_scores_init.sql) file in your Workbench which will create database, table (with 3 rows of data), stored procedure, and view
- import database from a self-contained file [user_scores_backup.sql](database%2Fuser_scores_backup.sql) which is located in the same directory
Once done the database should include 1 table (`quiz_scores`), 3 rows of data, and also:
- Stored procedure `AddUserScore`
- View `top_scores_view`

#### Config file
Once you have database on your SQL Workbench, you'll need to create a config.json file in config directory. It is included in .gitignore, so that your details stay safely on your machine.
We have included config_example.json, you can copy the details from that file to config.json and update your details: user, password, database name (if different), and host (if different)
Once you do that the app will be able to connect to your database.

### Run the App
To run the app go to app.py file in the root of the project. Run it from your machine. Open http://127.0.0.1:5000/ in a browser to view and navigate the app. It also works on mobile screens. 

## Usage
This app can be used in its whole to create a Flaks app for a quiz game with timer for each question and functionality to save user scores. Note the database does not store any sensitive user information.
What is more the QuizQuestions and QuizGame classes can be used as objects at another quiz app. 
1. QuizQuestion is a class that generates ten random questions of selected category from [The Trivia API](https://the-trivia-api.com/). 
- it has url setter method that takes category as argument. This is optional. Without it the object will connect to API to generate ten random questions from all categories
- using get_ten_rand_questions will generate questions in that category
- create_quiz_questions_dict turns questions into a dictionary. That dictionary can be then used by QuizGame class.
2. QuizGame is a class that contains quiz game mechanics. It takes a dictionary of quiz questions as argument. 
- it contains methods to check if there are questions left
- it updates question number
- it checks user answer
- it logs user answers against correct answers
Example usage of the two classes in a Python console, this is a simple run through the code and would need adjusting to your needs:
```
quiz_questions = QuizQuestions()
quiz_questions.url = "music"
questions_dict = quiz_questions.create_quiz_question_dict()
quiz_game = QuizGame(questions_dict)

while quiz_game.questions_left():
    print(quiz_game.current_question)
    print(quiz_game.current_answers)
    quiz_game.ask_question(int(input("Give index of the correct answer ")))

print("Quiz Finished")
print(quiz_game.user_answers)
print(f"Your score is: {quiz_game.score}")
```

## Testing
We used Python built in testing framework unittest to test individual functions and method. You can find all tests in tests directory. You can run each directory or test separately, or you can 


## Acknowledgments
[The Trivia API](https://the-trivia-api.com/)
Give credit to any external resources, libraries, or individuals that you found helpful or inspiring during the development of your project.
