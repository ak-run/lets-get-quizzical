import unittest

from models.quizgame_model import QuizGame


class TestQuizGame(unittest.TestCase):

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
        ]
        self.game = QuizGame(self.sample_questions)

    def test_questions_left_true(self):
        """testing when there are questions left"""
        self.assertTrue(self.game.questions_left())

    def test_questions_left_false(self):
        """testing when there are no questions left"""
        self.game.question_number = 2
        self.assertFalse(self.game.questions_left())

    def test_next_question(self):
        self.game.next_question()
        self.assertEqual(self.game.question_number, 1)
        self.assertEqual(self.game.current_question,
                         "Which planet is known as the Red Planet?")
        self.assertEqual(self.game.current_answers, [
                         "Mars", "Venus", "Jupiter", "Saturn"])
        self.assertEqual(self.game.current_correct_answer, 0)

    def test_ask_question_successful(self):
        # Test case for successful question asking
        question, answers = self.game.ask_question(user_answer=0)
        # Assumes next_question has been called once
        self.assertEqual(question, "Which planet is known as the Red Planet?")
        self.assertEqual(answers, ["Mars", "Venus", "Jupiter", "Saturn"])

    def test_ask_question_error(self):
        # Test case for an error during question asking
        # In this example, we'll simulate an error by passing an invalid user_answer
        with self.assertRaises(Exception) as context:
            self.game.ask_question(user_answer="Invalid Answer")

        # Check if the exception message contains the expected error message
        self.assertIn("Error asking question", str(context.exception))

    def test_ask_question_retrieve_user_answer(self):
        # Test case for retrieving and saving a user answer
        question, answers = self.game.ask_question(user_answer=2)

        # Check if the user answer has been saved correctly
        saved_user_answer = self.game.user_answers.get("What is the capital of France?")
        expected_answer = "Your answer: Rome, correct answer: Paris"
        self.assertEqual(saved_user_answer, expected_answer)

    def test_check_answer_correct(self):
        self.game.check_answer(1)
        self.assertEqual(self.game.score, 1)

    def test_check_answer_incorrect(self):
        self.game.check_answer(2)
        self.assertEqual(self.game.score, 0)

    def test_save_user_answer_correct(self):
        self.game.save_user_answer(1)
        self.assertEqual(self.game.user_answers, {
                         "What is the capital of France?": "Your answer, Paris, was correct"})

    def test_save_user_answer_incorrect(self):
        self.game.save_user_answer(2)
        self.assertEqual(
            self.game.user_answers,
            {"What is the capital of France?": "Your answer: Rome, correct answer: Paris"}
        )


if __name__ == "__main__":
    unittest.main()
