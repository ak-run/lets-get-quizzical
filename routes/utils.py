from models.question_model import QuizQuestions
from models.quizgame_model import QuizGame


def set_up_quiz_game(category):
    quiz_questions_obj = QuizQuestions()
    quiz_questions_obj.url = category
    quiz_questions = quiz_questions_obj.create_quiz_question_dict()
    quiz_game = QuizGame(quiz_questions)
    return quiz_game
