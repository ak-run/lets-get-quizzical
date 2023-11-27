import requests


class QuizQuestions:
    """Class to make API call and receive 10 random questions in a given category"""
    def __init__(self):
        self.question_categories = ["music", "sport_and_leisure", "film_and_tv", "arts_and_literature", "history",
                                    "society_and_culture", "science", "geography", "food_and_drink",
                                    "general_knowledge"]
        self._url = f"https://the-trivia-api.com/v2/questions"

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, category):
        if category in self.question_categories:
            self._url = f"{self._url}?categories={category}"
        else:
            raise ValueError(f"Invalid category: {category}")

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


# quiz = QuizQuestions()
# quiz.url = "music"
# questions = quiz.get_ten_rand_questions()
# print(questions)
