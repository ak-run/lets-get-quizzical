import unittest
import requests
from API.API_connection import get_ten_rand_questions, create_quiz_question_dict

class TestAPI(unittest.TestCase):
    """Testing the function get_10_rand_questions is valid, successfully connecting to API and returning
        a list of 10 dictionaries"""
    url = "https://the-trivia-api.com/v2/questions"

    def test_valid_API_connection(self):
        # test that API connection returns status code 200
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 200)


    def test_valid_get_ten_rand_questions(self):
        # checking that 10 dictionaries/ questions are returned
        player_one_q = get_ten_rand_questions(api_url="https://the-trivia-api.com/v2/questions")
        count = 0
        for question in player_one_q:
            count += 1
        self.assertEqual(count, 10)

    def test_invalid_url_get_ten_rand_questions(self):
        # testing assertion raised when the API url is invalid
        invalid_url = "blah"
        with self.assertRaises(SystemExit):
            get_ten_rand_questions(invalid_url)

    def test_HTTPSError_get_ten_rand_questions(self):
        # testing assertion raised with https error
        url_not_found = "https://the-trivia-api.com/v2/questionsss"
        with self.assertRaises(SystemExit):
            get_ten_rand_questions(url_not_found)


class TestCreateQuizQuestionDictFunction(unittest.TestCase):
    """Testing create_quiz_question_dict function has the correct output"""

    def test_valid_create_quiz_question_dict(self):
        # testing that a list of 10 dictionaries is created
        url = "https://the-trivia-api.com/v2/questions"
        result = get_ten_rand_questions(api_url=url)
        quiz = create_quiz_question_dict(api_result=result)
        count = 0
        for question in quiz:
            count += 1
        self.assertEqual(count, 10)


# TEST ATTEMPT
    def test_correct_answer_from_create_quiz_question_dict(self):
        # testing that the correct answer is formatted correctly- i.e. given correct index
        index_input = 1
        api_input = [{'category': 'arts_and_literature',
                      'correctAnswer': 'Ivan Turgenev',
                      'difficulty': 'hard',
                      'id': '622a1c397cc59eab6f950e61',
                      'incorrectAnswers': ['Leo Tolstoy', 'Henryk Sienkiewicz', 'Alphonse Daudet'],
                      'isNiche': False,
                      'question': {'text': "Which author wrote 'Poems in Prose'?"},
                      'regions': [],
                      'tags': ['arts_and_literature'],
                      'type': 'text_choice'}]



        expected = {'category': 'arts_and_literature',
                    'question': "Which author wrote 'Poems in Prose'?",
                    'answers': ["Leo Tolstoy, "
                                "Henryk Sienkiewicz",
                                "Alphonse Daudet's,",
                                "Ivan Turgenev"],
                    'correct_answer': "1"}   # THIS IS THE CORRECT ANSWER INDEX
        result = create_quiz_question_dict(api_input, index_input)
        self.assertEqual(expected, result)



if __name__ == '__main__':
    unittest.main()
