from flask import Blueprint, render_template
from models.question_model import QuizQuestions

from models.question_model import QuizQuestions

# blueprint for main page
main_bp = Blueprint("/", __name__, static_folder="static", template_folder="templates")



@main_bp.route("/")
def main():
    quiz = QuizQuestions()
    """Route for main page"""
    return render_template("quiz_setup.html", categories=quiz.question_categories)


@main_bp.route("/single/<category>")
def single(category):
    quiz = QuizQuestions()
    # select cateories
    quiz.url = category
    questions = quiz.create_quiz_question_dict()
    """Route for the single player page"""
    return render_template("single.html", questions=questions)

    

@main_bp.route("/how_to_play")
def how_to_play():
    """Route for the rules of the game"""
    return render_template("how_to_play.html")

@main_bp.route("/leaderboard")
def leaderboard():
    """Route for the leader board"""
    return render_template("leaderboard.html")


@main_bp.route("/setup")
def setup():
    """Route for the quiz setup"""
    return render_template("quiz_setup.html")