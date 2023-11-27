import requests
from pprint import pprint as pp
import random


# function to get 10 questions
def get_ten_rand_questions():
    try:
        url = "https://the-trivia-api.com/v2/questions"
        response = requests.get(url)
        questions = response.json()
        if response.status_code != 200:
            raise ConnectionError
    except requests.exceptions.RequestException as ce:
        print('''An error has occurred when trying to
              connect to the API: {} '''.format(ce))
    else:
        return questions


# pp(get_ten_rand_questions())


def create_quiz_question_dict():
    # creates a dict with q's and a's. 4 possible answers but correct answer is given an index 0-3
    quiz_questions = []
    for raw_question in get_ten_rand_questions():
        correct_ans_index = random.randint(0, 3)
        ans = raw_question['incorrectAnswers']
        ans.insert(correct_ans_index, raw_question['correctAnswer'])
        quiz_dict = {
            'category': raw_question['category'],
            'question': raw_question['question']["text"],
            'answers': ans,
            'correct_answer': correct_ans_index
        }
        quiz_questions.append(quiz_dict)
    return quiz_questions


print(create_quiz_question_dict())
