import random
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

    def create_quiz_question_dict(self):
        """creates a dict with q's and a's. 4 possible answers but correct answer is given an index 0-3"""
        quiz_questions = []
        for raw_question in self.get_ten_rand_questions():
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
        

    # def get_questions(self):
    #     # Get questions from a specific category
    #     raw_questions = self.get_ten_rand_questions(self.questions_category)
    #     return raw_questions
    

