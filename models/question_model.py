import random
import requests


class QuizQuestions:
    """
    Class to make API call and receive 10 random questions in a given category
    Attributes:
        question_categories: A list of available question categories.
        _url : The base URL for making API calls.
    """
    # Question categories are a class variable because they are the same for all instances of the class
    question_categories = ["music", "sport_and_leisure", "film_and_tv", "arts_and_literature", "history",
                           "society_and_culture", "science", "geography", "food_and_drink",
                           "general_knowledge"]

    def __init__(self):
        self._url = f"https://the-trivia-api.com/v2/questions"

    @property
    def url(self):
        """Get the current API URL."""
        return self._url

    @url.setter
    def url(self, category):
        """
        Set the API URL by adding the chosen question category.
        Parameters: category: the chosen question category.
        Raises ValueError if the provided category is invalid.
        """
        if category in self.question_categories:
            self._url = f"{self._url}?categories={category}"
        else:
            raise ValueError(f"Invalid category: {category}")

    def get_ten_rand_questions(self):
        """
        Make an API call to get 10 random questions.
        Returns: the JSON response containing 10 random questions.
        Raises ConnectionError if the API call is unsuccessful.
        """
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
        """
        Create a dictionary with questions and answers.
        Returns: a list of dictionaries, each containing a question and its details.
        """
        quiz_questions = []
        for raw_question in self.get_ten_rand_questions():
            # generates a random integer between 0 and 3 to determine the index at which the correct answer should
            # be inserted among the incorrect answers
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
