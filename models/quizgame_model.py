import requests
import mysql.connector
import unittest
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

"""

---- API CALL CLASS WRITTEN ALREADY SO PROB DON'T NEED THIS -----
class QuizQuestions:
    def __init__(self, category):
        self.url = "https://opentdb.com/api.php?type=multiple"
        self.questions_category = category

    def api_call(self, category):
        # Get data from API
        try:
            response = requests.get(f"{self.url}&category={category}")
            response.raise_for_status()
            data = response.json()

            if data['response_code'] != 0:
                raise Exception('Bad API data')

            raw_questions = data['results']
            return raw_questions
        except requests.exceptions.RequestException as e:
            raise Exception(f'Error making API request: {e}')

    def get_questions(self):
        # Get questions from a specific category
        try:
            raw_questions = self.api_call(self.questions_category)
            return raw_questions
        except Exception as e:
            raise Exception(f'Error getting questions: {e}')

"""


class QuizGame:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def questions_left(self):
        """Check if questions are left in the set"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Go to the next question"""
        self.question_number += 1

    def ask_question(self):
        """Loop through the question list"""
        try:
            for question in self.question_list:
                # Display question to players (socket communication)
                emit('question', {
                     'question': question['question'], 'answers': question['answers']})

                user_answer = input(
                    "Choose the number corresponding to the correct answer: ")
                correct_answer = question['correct_answer']

                if int(user_answer) == correct_answer + 1:
                    self.score += 1
                    return "Nice one! That's the right answer! "
                else: 
                    self.next_question()
                    return "Sorry, that's not the right answer. "
        except Exception as e:
            raise Exception(f'Error asking question: {e}')

    def get_correct_answer(self, question):
        """Get the correct answer for a question"""
        return question['correct_answer']

    def check_answer(self, correct_answer, user_answer):
        """Check if the user's answer is correct and update the score"""
        if int(user_answer) == correct_answer + 1:
            print("Nice one! That's the right answer! ")
            self.score += 1
        else:
            print("Sorry, that's not the right answer. ")

    def save_user_answers(self):
        """Save user answers, maybe in a dictionary?"""
        # self.user_answers[question['question']] = user_answer   NEED TO CHECK THIS

    def display_correct_answers(self):
        """Display to users their answers vs. correct answers"""
        try:
            for question in self.question_list:
                correct_answer = question['correct_answer']
                user_answer = self.user_answers[question['question']]

                if correct_answer == user_answer:
                    print(
                        f"Your answer to the question '{question['question']}' was correct!")
                else:
                    print(
                        f"Your answer to the question '{question['question']}' was incorrect. The correct answer was '{correct_answer}'.")
        except Exception as e:
            raise Exception(f'Error displaying correct answers: {e}')


class TestQuizGame(unittest.TestCase):
    def test_questions_left(self):
        game = QuizGame([])
        self.assertFalse(game.questions_left())

    def test_next_question(self):
        game = QuizGame([])
        game.next_question()
        self.assertEqual(game.question_number, 1)

    def test_get_correct_answer(self):
        game = QuizGame([{'correct_answer': 1}])
        correct_answer = game.get_correct_answer(game.question_list[0])
        self.assertEqual(correct_answer, 1)

    def test_check_answer_correct(self):
        game = QuizGame([])
        game.check_answer(1, 1)
        self.assertEqual(game.score, 1)

    def test_check_answer_incorrect(self):
        game = QuizGame([])
        game.check_answer(1, 2)
        self.assertEqual(game.score, 0)


if __name__ == "__main__":
    unittest.main()


"""

----- PREVIOUS DEMO CODE -----

class QuizGame:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def questions_left(self):
        # Check if questions are left in the set
        return self.question_number < len(self.question_list)

    def next_question(self):
        # Go to the next question
        self.question_number += 1

    def ask_question(self):
        # Loop through the question list
        for question in self.question_list:
            pass

    def get_correct_answer(self, question):
        # Get the correct answer for a question
        return question['correct_answer']

    def check_answer(self, correct_answer, user_answer):
        # Check if the user's answer is correct and update the score
        if int(user_answer) == correct_answer + 1:
            print("Nice one! That's the right answer! ")
            self.score += 1
        else:
            print("Sorry, that's not the right answer. ")

    def save_user_answers(self):
        # Save user answers, maybe in a dictionary?
        pass

    def display_correct_answers(self):
        # Display to users their answers vs. correct answers
        pass
"""
