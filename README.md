# Project Name

Short description or tagline of your project.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
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
Classes
Provide examples and instructions on how to use your project. Include code snippets if necessary.

## Testing

## Contributing

Explain how others can contribute to your project. Include guidelines for submitting bug reports, feature requests, or code contributions.

## Acknowledgments

Give credit to any external resources, libraries, or individuals that you found helpful or inspiring during the development of your project.
