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
        """Testing the next question is asked"""
        self.game.next_question()
        self.assertEqual(self.game.question_number, 1)
        self.assertEqual(self.game.current_question, "Which planet is known as the Red Planet?")
        self.assertEqual(self.game.current_answers, ["Mars", "Venus", "Jupiter", "Saturn"])
        self.assertEqual(self.game.current_correct_answer, 0)

    def test_retrieve_user_answer(self):
        """TBA"""
        pass

    def test_check_answer_correct(self):
        self.game.check_answer(1)
        self.assertEqual(self.game.score, 1)

    def test_check_answer_incorrect(self):
        self.game.check_answer(2)
        self.assertEqual(self.game.score, 0)

    def test_save_user_answer_correct(self):
        self.game.save_user_answer(1)
        self.assertEqual(self.game.user_answers, {"What is the capital of France?": "Your answer, Paris, was correct"})

    def test_save_user_answer_incorrect(self):
        self.game.save_user_answer(2)
        self.assertEqual(
            self.game.user_answers,
            {"What is the capital of France?": "Your answer: Rome, correct answer: Paris"}
        )


if __name__ == "__main__":
    unittest.main()
