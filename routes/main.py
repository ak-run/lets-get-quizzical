from flask import Blueprint, render_template, session, request
from models.question_model import QuizQuestions

from models.question_model import QuizQuestions

# blueprint for main page
main_bp = Blueprint("/", __name__, static_folder="static", template_folder="templates")



@main_bp.route("/")
def main():
    quiz = QuizQuestions()
    """Route for main page"""
    return render_template("quiz_setup.html", categories=quiz.question_categories)


@main_bp.route("/single", methods=["POST", "GET"])
def single():
    quiz = QuizQuestions()
    if request.method == 'POST':
        session.permanent = True
        
    questions = quiz.create_quiz_question_dict()
        # quiz.url = category
    session['quiz_questions'] = questions
    for question in questions:
        current_question = questions[0]
        # return current_question
            # questions.loop.index +=1
        
        
    
    return render_template("single.html", questions=questions, current_question=current_question)

    

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