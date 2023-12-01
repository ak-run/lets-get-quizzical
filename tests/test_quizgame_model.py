import unittest
from models.quizgame_model import QuizGame


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
