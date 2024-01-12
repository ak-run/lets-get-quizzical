import unittest
from collections import OrderedDict
from models.quizgame_model import QuizGame


class TestQuizGame(unittest.TestCase):
    """
    Testing the quizgame_model for the correct quiz flow:
        - getting, checking, and saving users answers
        - progressing to the next question if there are remaining questions
    """

    def setUp(self):
        """Sample questions for testing"""
        self.sample_questions = [
            {
                "question": "What is the capital of France?",
                "answers": ["Berlin", "Paris", "Rome", "Madrid"],
                "correct_answer": 1,
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "answers": ["Mars", "Venus", "Jupiter", "Saturn"],
                "correct_answer": 0,
            },
            {
                "question": "Which famous scientist developed the theory of relativity?",
                "answers": ["Isaac Newton", "Galileo Galilei", "Albert Einstein", "Niels Bohr"],
                "correct_answer": 2,
            },
            {
                "question": "What is the largest mammal on Earth?",
                "answers": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
                "correct_answer": 1,
            }
        ]
        self.game = QuizGame(self.sample_questions)

    def test_to_dict(self):
        """
        Test if to_dict correctly create a dictionary representing instance of QuizGame class
        """
        self.game.ask_question(2)
        result = self.game.to_dict()
        expected_result = {'current_answers': ['Mars', 'Venus', 'Jupiter', 'Saturn'],
                           'current_correct_answer': 0,
                           'current_question': 'Which planet is known as the Red Planet?',
                           'question_list': [{
                               "question": "What is the capital of France?",
                               "answers": ["Berlin", "Paris", "Rome", "Madrid"],
                               "correct_answer": 1,
                           },
                               {
                                   "question": "Which planet is known as the Red Planet?",
                                   "answers": ["Mars", "Venus", "Jupiter", "Saturn"],
                                   "correct_answer": 0,
                               },
                               {
                                   "question": "Which famous scientist developed the theory of relativity?",
                                   "answers": ["Isaac Newton", "Galileo Galilei", "Albert Einstein", "Niels Bohr"],
                                   "correct_answer": 2,
                               },
                               {
                                   "question": "What is the largest mammal on Earth?",
                                   "answers": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
                                   "correct_answer": 1,
                               }],
                           'question_number': 1,
                           'score': 0,
                           'user_answers': {'01. What is the capital of France?': 'Your answer: Rome, '
                                                                                  'correct answer: '
                                                                                  'Paris'}}
        self.assertEqual(result, expected_result)

    def test_from_dict(self):
        """
        Test if from_dict correctly creates instance of QuizGame class from a dictionary
        """
        # Sample data for testing from_dict
        sample_data = {
            "question_number": 1,
            "score": 10,
            "current_question": "Which planet is known as the Red Planet?",
            "current_answers": ["Mars", "Venus", "Jupiter", "Saturn"],
            "current_correct_answer": 0,
            "user_answers": {"01. What is the capital of France?": "Your answer: Rome, correct answer: Paris"},
            "question_list": [
                {
                    "question": "What is the capital of France?",
                    "answers": ["Berlin", "Paris", "Rome", "Madrid"],
                    "correct_answer": 1,
                },
                {
                    "question": "Which planet is known as the Red Planet?",
                    "answers": ["Mars", "Venus", "Jupiter", "Saturn"],
                    "correct_answer": 0,
                },
            ],
        }

        # Create a QuizGame instance using from_dict
        quiz_game_instance = QuizGame.from_dict(self.sample_questions, sample_data)

        # Check if the instance attributes match the sample data
        self.assertEqual(quiz_game_instance.question_number, sample_data["question_number"])
        self.assertEqual(quiz_game_instance.score, sample_data["score"])
        self.assertEqual(quiz_game_instance.current_question, sample_data["current_question"])
        self.assertEqual(quiz_game_instance.current_answers, sample_data["current_answers"])
        self.assertEqual(quiz_game_instance.current_correct_answer, sample_data["current_correct_answer"])
        self.assertEqual(quiz_game_instance.user_answers, sample_data["user_answers"])
        self.assertEqual(quiz_game_instance.question_list, sample_data["question_list"])

    def test_questions_left_true(self):
        """testing when there are questions left"""
        self.assertTrue(self.game.questions_left())

    def test_questions_left_false(self):
        """testing when there are no questions left"""
        self.game.question_number = 5
        self.assertFalse(self.game.questions_left())

    def test_next_question(self):
        """Testing all elements of the next question is shown"""
        self.game.next_question()
        self.assertEqual(self.game.question_number, 1)
        self.assertEqual(self.game.current_question,
                         "Which planet is known as the Red Planet?")
        self.assertEqual(self.game.current_answers, [
            "Mars", "Venus", "Jupiter", "Saturn"])
        self.assertEqual(self.game.current_correct_answer, 0)

    def test_ask_question_successful(self):
        """"Test case for successful question asking"""
        self.game.ask_question(user_answer=0)
        # Assumes next_question has been called once
        self.assertEqual(self.game.current_question, "Which planet is known as the Red Planet?")
        self.assertEqual(self.game.current_answers, ["Mars", "Venus", "Jupiter", "Saturn"])

    def test_ask_question_error(self):
        """Testing an exception is raised with an invalid user answer"""
        with self.assertRaises(Exception) as context:
            self.game.ask_question(user_answer="Invalid Answer")

        # Check if the exception message contains the expected error message
        self.assertIn("Error asking question", str(context.exception))

    def test_ask_question_retrieve_user_answer(self):
        """Testing the function retrieves and saves the user answer"""
        # test case for retrieving and saving user answer
        self.game.ask_question(user_answer=2)

        # Check if the user answer has been saved correctly
        saved_user_answer = self.game.user_answers.get("01. What is the capital of France?")
        expected_answer = "Your answer: Rome, correct answer: Paris"
        self.assertEqual(saved_user_answer, expected_answer)

    def test_check_answer_correct(self):
        """Testing that the user gets a point when inputting the correct answer for Q1 of the sample questions"""
        self.game.check_answer(1)
        self.assertEqual(self.game.score, 1)

    def test_check_answer_incorrect(self):
        """Testing that the user does NOT get a point when inputting the WRONG answer for Q1 of the sample questions"""
        self.game.check_answer(2)
        self.assertEqual(self.game.score, 0)

    def test_save_user_answer_correct(self):
        """Testing the function creates the expected Q & A dictionary"""
        self.game.save_user_answer(1)
        self.assertEqual(self.game.user_answers, {
            "01. What is the capital of France?": "Your answer, Paris, was correct"})

    def test_save_user_answer_correct_order(self):
        """Testing the users answers will be saved in order from Q1-Q10"""
        self.game.ask_question(2)
        self.game.ask_question(1)
        self.game.ask_question(2)
        self.game.ask_question(3)

        expected_result = {
            '01. What is the capital of France?': 'Your answer: Rome, correct answer: Paris',
            '02. Which planet is known as the Red Planet?': 'Your answer: Venus, correct answer: Mars',
            '03. Which famous scientist developed the theory of relativity?': 'Your answer, Albert Einstein, '
                                                                              'was correct',
            '04. What is the largest mammal on Earth?': 'Your answer: Hippopotamus, correct answer: Blue Whale'}

        # Converting results into OrderedDict to check if the questions are saved in the correct order
        self.assertEqual(OrderedDict(self.game.user_answers), OrderedDict(expected_result))

    def test_save_user_answer_incorrect(self):
        """Testing that incorrect answers are still correctly added to the users answer dictionary"""
        self.game.save_user_answer(2)
        self.assertEqual(
            self.game.user_answers,
            {"01. What is the capital of France?": "Your answer: Rome, correct answer: Paris"}
        )


if __name__ == "__main__":
    unittest.main()
