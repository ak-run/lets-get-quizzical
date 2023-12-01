import requests
from pprint import pprint as pp
import random

# API url for quiz questions
url = "https://the-trivia-api.com/v2/questions"


# function to get 10 questions
def get_ten_rand_questions(api_url):
    try:
        response = requests.get(api_url)
        questions = response.json()
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print("HTTP Error: {}".format(http_err))
        raise SystemExit(http_err)
    except requests.exceptions.RequestException as ce:
        # this exception covers all potential requesting errors - Timeout, HTTPError, TooManyRedirects
        print('''An error has occurred when trying to
              connect to the API: {} '''.format(ce))
        raise SystemExit(ce)
    else:
        return questions


# pp(get_ten_rand_questions(url))

# CORRECT FUNCTION:
# quiz_questions = []
# def create_quiz_question_dict(api_result):  # get_ten_rand_questions(url): should be the parameter for function call
#  # formats the API results. 4 possible answers but correct answer is inserted at a random index 0-3 which is recorded
#     for raw_question in api_result:
#         correct_ans_index = random.randint(0, 3)
#         ans = raw_question['incorrectAnswers']
#         ans.insert(correct_ans_index, raw_question['correctAnswer'])
#         quiz_dict = {
#             'category': raw_question['category'],
#             'question': raw_question['question']["text"],
#             'answers': ans,
#             'correct_answer': correct_ans_index
#         }
#         quiz_questions.append(quiz_dict)
#     return quiz_questions


# ATTEMPT TO MAKE THE FUNCTION BETTER FORMATTED- to test if the index given actually matches the correct answer
quiz_questions = []  # the formatted dictionary is appended to this variable


def get_rand_index():
    return random.randint(0, 3)


def create_quiz_question_dict(api_result, input_index):
    """ get_ten_rand_questions(url), and get_random_index() should be the parameters when function is called"""
    # formats the API results. 4 possible answers but correct answer is inserted at a random index 0-3 which is recorded
    for question in api_result:
        correct_ans_index = input_index
        ans = question['incorrectAnswers']
        ans.insert(correct_ans_index, question['correctAnswer'])
        quiz_dict = {
            'category': question['category'],
            'question': question['question']["text"],
            'answers': ans,
            'correct_answer': correct_ans_index
        }
        quiz_questions.append(quiz_dict)
    return quiz_questions


create_quiz_question_dict(get_ten_rand_questions(url), get_rand_index())
print(quiz_questions)


