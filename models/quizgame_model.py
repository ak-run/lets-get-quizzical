class QuizGame:
    """
    A class representing a quiz game.

    Attributes:
    - question_number: Current question index.
    - score: Integer with current score.
    - question_list: List of quiz questions and answers.
    - current_question: Text of the current question.
    - current_answers: List of possible answers for the current question.
    - current_correct_answer: Index of the correct answer for the current question.
    - user_answers: Dictionary to store user's answers.

    Methods:
    - to_dict(): Convert the QuizGame instance to a dictionary.
    - from_dict(cls, question_list, data): Create a QuizGame instance from a dictionary.
    - questions_left(): Check if there are more questions left.
    - next_question(): Move to the next question.
    - ask_question(user_answer): Ask the current question, check the answer, save user answer, and move to the next question.
    - check_answer(user_answer): Check if the user's answer is correct, update the score.
    - save_user_answer(user_answer): Save the user's answer for display at the end of the quiz.
    """
    def __init__(self, question_list):
        """
        Initialize a QuizGame instance with question_list as parameter, it contains quiz questions and answers.
        """
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        self.current_question = self.question_list[self.question_number]["question"]
        self.current_answers = self.question_list[self.question_number]["answers"]
        self.current_correct_answer = self.question_list[self.question_number]["correct_answer"]
        self.user_answers = {}

    def to_dict(self):
        """
        Convert the QuizGame instance to a dictionary.
        """
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
        """
        Create a QuizGame instance from a dictionary.
        Parameters:
        - question_list: List of quiz questions and answers.
        - data: Dictionary containing QuizGame data.
        Returns: An instance of the QuizGame class.
        """
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
        """Check if questions are left in the set, returns True or False"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Moves to the next question.
        Updates class attributes: question number, current question, current answers and current correct answer
        """
        self.question_number += 1
        if self.questions_left():
            self.current_question = self.question_list[self.question_number]["question"]
            self.current_answers = self.question_list[self.question_number]["answers"]
            self.current_correct_answer = self.question_list[self.question_number]["correct_answer"]

    def ask_question(self, user_answer):
        """
        Ask the current question, check the answer, save user answer, and move to the next question.
        Parameters: user_answer: The user's answer to the current question.
        """
        try:
            if user_answer is None:
                self.save_user_answer(user_answer)
                self.next_question()
            else:
                self.check_answer(user_answer)
                self.save_user_answer(user_answer)
                self.next_question()

        except Exception as e:
            raise Exception(f'Error asking question: {e}')

    def check_answer(self, user_answer):
        """
        Check if the user's answer is correct, update the score and save the answer
        Parameters: user_answer: The user's answer to the current question.
        """
        if user_answer == self.current_correct_answer:
            self.score += 1
        self.save_user_answer(user_answer)

    def save_user_answer(self, user_answer):
        """
        Saves user questions and answers in a dictionary so they can be displayed at the end of the quiz
        A question is saved as a key and a string with correct answer and user answer is added as value
        Parameters: user_answer: The user's answer to the current question.
        """
        question_number_display = self.question_number + 1
        formatted_question_number = f"{question_number_display:02d}"
        question_key = f"{formatted_question_number}. {self.current_question}"
        if user_answer is None:
            self.user_answers[question_key] = "The time run out and you didn't answer this question"
        else:
            user_answer_text = self.question_list[self.question_number]["answers"][user_answer]
            correct_answer_text = self.question_list[self.question_number]["answers"][self.current_correct_answer]
            if user_answer == self.current_correct_answer:
                self.user_answers[question_key] = f"Your answer, {user_answer_text}, was correct"
            else:
                self.user_answers[question_key] = f"Your answer: {user_answer_text}, " \
                                                       f"correct answer: {correct_answer_text}"
