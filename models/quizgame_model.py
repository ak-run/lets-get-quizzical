from flask import Flask
# from flask_socketio import SocketIO, emit
from models.question_model import QuizQuestions

app = Flask(__name__)
# socketio = SocketIO(app)


class QuizGame:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        self.current_question = self.question_list[self.question_number]["question"]
        self.current_answers = self.question_list[self.question_number]["answers"]
        self.current_correct_answer = self.question_list[self.question_number]["correct_answer"]
        self.user_answers = {}

    def to_dict(self):
        return {
            "question_number": self.question_number,
            "score": self.score,
            "current_question": self.current_question,
            "current_answers": self.current_answers,
            "current_correct_answer": self.current_correct_answer,
            "user_answers": self.user_answers,
            "question_list": self.question_list
        }

    @classmethod
    def from_dict(cls, question_list, data):
        quiz_game = cls(question_list)
        quiz_game.question_number = data["question_number"]
        quiz_game.score = data["score"]
        quiz_game.current_question = data["current_question"]
        quiz_game.current_answers = data["current_answers"]
        quiz_game.current_correct_answer = data["current_correct_answer"]
        quiz_game.user_answers = data["user_answers"]
        quiz_game.question_list = data["question_list"]
        return quiz_game

    def questions_left(self):
        """Check if questions are left in the set"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Update class attributes: question number, current question, current answers and current correct answer"""
        self.question_number += 1
        if self.questions_left():
            self.current_question = self.question_list[self.question_number]["question"]
            self.current_answers = self.question_list[self.question_number]["answers"]
            self.current_correct_answer = self.question_list[self.question_number]["correct_answer"]

    def ask_question(self, user_answer):
        """Ask current question and use class methods to check answer, save user answer and go to next question"""
        try:
            if user_answer is None:
                self.next_question()
            else:
                self.check_answer(user_answer)
                self.save_user_answer(user_answer)
                self.next_question()
            return self.current_question, self.current_answers

        except Exception as e:
            raise Exception(f'Error asking question: {e}')

    def check_answer(self, user_answer):
        """Check if the user's answer is correct, update the score and save the answer"""
        if user_answer == self.current_correct_answer:
            self.score += 1
        self.save_user_answer(user_answer)

    def save_user_answer(self, user_answer):
        """
        Saves user questions and answers in a dictionary so they can be displayed at the end of the quiz
        A question is saved as a key and a string with correct answer and user answer is added as value
        """
        user_answer_text = self.question_list[self.question_number]["answers"][user_answer]
        correct_answer_text = self.question_list[self.question_number]["answers"][self.current_correct_answer]
        if user_answer == self.current_correct_answer:
            self.user_answers[self.current_question] = f"Your answer, {user_answer_text}, was correct"
        else:
            self.user_answers[self.current_question] = f"Your answer: {user_answer_text}, " \
                                                       f"correct answer: {correct_answer_text}"

# ----------------------------------------
# TO SEE IT's WORKING UNCOMMENT TEXT BELOW
# ----------------------------------------
# quiz = QuizQuestions()
# quiz.url = "music"
# questions_dict = quiz.create_quiz_question_dict()
# quiz = QuizGame(questions_dict)
#
# while quiz.questions_left():
#     quiz.ask_question(1)
#
# print("Quiz Finished")
# print(quiz.user_answers)
# print(quiz.score)
