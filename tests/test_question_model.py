import unittest
import requests
from models.question_model import QuizQuestions


class TestQuestionModel(unittest.TestCase):

    def setUp(self):
        self.questions = QuizQuestions()

    def test_valid_api_connection(self):
        response = requests.get(self.questions.url)
        self.assertEqual(response.status_code, 200)

    def test_invalid_api_connection(self):
        response = requests.get("https://the-trivia-api.com/v2/questions2")
        self.assertEqual(response.status_code, 404)

    def test_valid_url_setter(self):
        self.questions.url = "music"
        result = self.questions._url
        expected_result = "https://the-trivia-api.com/v2/questions?categories=music"
        self.assertEqual(result, expected_result)

    def test_invalid_url_setter(self):
        with self.assertRaises(ValueError):
            self.questions.url = "wrong category"

    def test_valid_get_ten_rand_questions(self):
        """Test that 10 dictionaries are retrieved from API, 1 for each question"""
        player_one_q = self.questions.get_ten_rand_questions(self._url)
        self.assertEqual(len(player_one_q), 10)

    def test_invalid_get_ten_rand_questions(self):
        """""Testing an exception is raised when cannot connect to the API"""
        self._url = "invalid url"
        with self.assertRaises(requests.exceptions.RequestException):
            self.questions.get_ten_rand_questions(self._url)

    def test_valid_create_quiz_question_dict(self):
        """Test that 10 finalised dictionaries are created, 1 for each question"""
        quiz = self.questions.create_quiz_question_dict()
        self.assertEqual(len(quiz), 10)


if __name__ == '__main__':
    unittest.main()
