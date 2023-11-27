
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
