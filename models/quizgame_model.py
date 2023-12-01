from flask import Flask
from flask_socketio import SocketIO, emit
from models.question_model import QuizQuestions

app = Flask(__name__)
socketio = SocketIO(app)

quiz = QuizQuestions()
quiz.url = "music"
questions_dict = quiz.create_quiz_question_dict()


class QuizGame:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        self.current_question = self.question_list[self.question_number]["question"]
        self.current_answers = self.question_list[self.question_number]["answers"]
        self.current_correct_answer = self.question_list[self.question_number]["correct_answer"]
        self.user_answers = {}

    def questions_left(self):
        """Check if questions are left in the set"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Go to the next question"""
        self.question_number += 1
        if self.questions_left():
            self.current_question = self.question_list[self.question_number]["question"]
            self.current_answers = self.question_list[self.question_number]["answers"]
            self.current_correct_answer = self.question_list[self.question_number]["correct_answer"]

    def ask_question(self):
        """Ask current question"""
        try:
            print(self.current_question, self.current_answers)
            user_answer = int(input("ANSWER "))
            self.check_answer(user_answer)
            self.save_user_answer(user_answer)
            self.next_question()

        except Exception as e:
            raise Exception(f'Error asking question: {e}')

    def get_user_answer(self):
        """Get the user's answer from socket communication"""
        user_answer = None
        while user_answer is None:
            socketio.sleep(1)  # Wait for 1 second before checking again
            user_answer = self.retrieve_user_answer_from_socket()
        return int(user_answer)

    def retrieve_user_answer_from_socket(self):
        """Retrieve the user's answer from socket communication"""
        return 1  # for now to return something

    def check_answer(self, user_answer):
        """Check if the user's answer is correct and update the score"""
        if user_answer == self.current_correct_answer:
            self.score += 1
        self.save_user_answer(user_answer)

    def save_user_answer(self, user_answer):
        """
        Saves user questions and answers in a dictionary so they can be displayed at the end of the quiz
        A question is saved as a key and a string with correct answer and user answer is added as value
        """
        # question = self.question_list[self.question_number]["question"]
        # correct_answer_idx = self.question_list[self.question_number]["correct_answer"]
        # correct_answer = self.question_list[self.question_number]["answers"][correct_answer_idx]
        # user_answer = self.question_list[self.question_number]["answers"][user_answer_idx]
        if user_answer == self.current_correct_answer:
            self.user_answers[self.current_question] = f"Your answer {user_answer} was correct"
        else:
            self.user_answers[self.current_question] = f"Your answer: {user_answer}, correct answer: {self.current_correct_answer}"


quiz = QuizGame(questions_dict)

while quiz.questions_left():
    quiz.ask_question()

print("Quiz Finished")
print(quiz.user_answers)
print(quiz.score)

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
        
      def display_correct_answers(self):
        try:
            for question in self.user_answers:
                correct_answer = question['correct_answer']
                user_answer = self.user_answers[question['question']]

                if correct_answer == user_answer:
                    return f"Your answer to the question '{question['question']}' was correct!"
                else:
                    return f"Your answer to the question '{question['question']}' was incorrect. The correct answer was '{correct_answer}'."
        except Exception as e:
            raise Exception(f'Error displaying correct answers: {e}')
"""
