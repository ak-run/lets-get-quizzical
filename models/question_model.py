# class Question:
#    pass

import requests


class QuizQuestions:
    def __init__(self, category):
        self.url = "https://opentdb.com/api.php?type=multiple"
        self.questions_category = category

    def api_call(self, category):
        # Get data from API
        response = requests.get(f"{self.url}&category={category}")
        data = response.json()

        if data['response_code'] != 0:
            exit('Bad API data')

        raw_questions = data['results']
        return raw_questions

    def get_questions(self):
        # Get questions from a specific category
        raw_questions = self.api_call(self.questions_category)
        return raw_questions
