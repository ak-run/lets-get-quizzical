import requests
from pprint import pprint as pp

# function to get 10 questions- produces a list of dictionaries
def get_ten_rand_questions():
    try:
        url = "https://the-trivia-api.com/v2/questions"
        response = requests.get(url)
        questions = response.json()
        if response.status_code != 200:
            raise ConnectionError
    except ConnectionError as ce:
        print('''An error has occurred when trying to
              connect to the API: {} '''.format(ce))
    else:
        return questions

# pp(get_ten_rand_questions())

# player_one_q = get_ten_rand_questions()





