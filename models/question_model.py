import requests


class QuizQuestions:
    def __init__(self, category):
        self._url = f"https://the-trivia-api.com/v2/questions?categories={category}"

    def get_ten_rand_questions(self):
        try:
            response = requests.get(self._url)
            questions = response.json()
            if response.status_code != 200:
                raise ConnectionError
        except requests.exceptions.RequestException as ce:
            print('''An error has occurred when trying to
                  connect to the API: {} '''.format(ce))
        else:
            return questions

    # def get_questions(self):
    #     # Get questions from a specific category
    #     raw_questions = self.get_ten_rand_questions(self.questions_category)
    #     return raw_questions


# quiz = QuizQuestions("music")
# questions = quiz.get_ten_rand_questions()
# print(questions)
