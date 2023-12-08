from flask import Blueprint, render_template, session, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField

from models.question_model import QuizQuestions
from models.quizgame_model import QuizGame

# blueprint for main page
main_bp = Blueprint("/", __name__, static_folder="static", template_folder="templates")


class QuestionForm(FlaskForm):
    user_answer = RadioField('Answer', choices=[], coerce=int)
    submit = SubmitField("Submit")


@main_bp.route("/")
def main():
    quiz = QuizQuestions()
    """Route for main page"""
    return render_template("quiz_setup.html", categories=quiz.question_categories)


@main_bp.route("/single", methods=["POST", "GET"])
def single():
    form = QuestionForm()
    quiz_questions_obj = QuizQuestions()
    quiz_questions = quiz_questions_obj.create_quiz_question_dict()
    quiz_game = QuizGame(quiz_questions)
    form.validate_on_submit()
    request.method = 'POST'
    session.permanent = True
    user_answer = form.user_answer.data
    # quiz_game.ask_question(user_answer)
    current_question = quiz_game.current_question
    question_number = quiz_game.question_number + 1
    current_answers = quiz_game.current_answers
    session["user_answer"] = user_answer
    session['quiz_questions'] = quiz_game.question_list

    return render_template("single.html",
                           form=form,
                           questions=quiz_questions,
                           user_answer=user_answer,
                           current_question=current_question,
                           question_number=question_number,
                           current_answers=current_answers)


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
