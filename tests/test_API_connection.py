from unittest import TestCase
import requests
from API.API_connection import get_ten_rand_questions

class TestAPI(TestCase):
    url = "https://the-trivia-api.com/v2/questions"


    def test_API_connection(self):
        # test that API connection returns status code 200
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_get_ten_rand_questions(self):
        # checking that 10 dictionaries/ questions are returned
        player_one_q = get_ten_rand_questions()
        count = 0
        for question in player_one_q:
            count += 1
        self.assertEqual(count, 10)
