from flask import Blueprint, render_template, session, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, StringField

from models.db_connection_model import DatabaseConnection, config
from models.leaderboard_model import Leaderboard
from models.question_model import QuizQuestions
from models.quizgame_model import QuizGame

# blueprint for main page
main_bp = Blueprint("/", __name__, static_folder="static", template_folder="templates")

# Flask forms
class QuestionForm(FlaskForm):
    user_answer = RadioField('Answer', choices=[], coerce=int)
    submit = SubmitField("Submit")

class ProfileForm(FlaskForm):
    nickname = StringField('Nickname')
    submit = SubmitField('Start Quiz')


class LeaderboardForm(FlaskForm):
    """pass because there are no special fields in the Flask Form needed"""
    pass


conn = DatabaseConnection(config)
conn.get_connection_to_db()

@main_bp.route("/", methods=["GET", "POST"])
def main():
    form = ProfileForm()
    avatar_filenames = [f"{i}.png" for i in range(1, 13)]
    return render_template("index.html", form=form, avatar_filenames=avatar_filenames)

@main_bp.route("/start_quiz", methods=["POST"])
def start_quiz():
    form = ProfileForm()
    if form.validate_on_submit():
        session['nickname'] = form.nickname.data
        session['avatar'] = request.form['avatar']
        quiz = QuizQuestions()
        return render_template("quiz_setup.html", categories=quiz.question_categories)

@main_bp.route("/play_quiz", methods=["POST", "GET"])
def play_quiz():
    """Route for quiz"""
    form = QuestionForm()

    if "quiz_game" not in session:
        quiz_questions_obj = QuizQuestions()
        category = request.args.get("category")
        quiz_questions_obj.url = category
        quiz_questions = quiz_questions_obj.create_quiz_question_dict()
        quiz_game = QuizGame(quiz_questions)
        session["quiz_game"] = quiz_game.to_dict()
        current_question = session["quiz_game"]["current_question"]
        question_number = session["quiz_game"]["question_number"]
        current_answers = session["quiz_game"]["current_answers"]
        session["quiz_questions"] = session["quiz_game"]["question_list"]
        current_user_answers = None
        current_user_score = None
        questions_left = True
    else:
        quiz_questions = session["quiz_game"]["question_list"]
        user_answer = form.user_answer.data
        quiz_game = QuizGame.from_dict(quiz_questions, session["quiz_game"])
        quiz_game.ask_question(user_answer)
        session["quiz_game"] = quiz_game.to_dict()
        # Fetch the updated values from the session
        question_number = session["quiz_game"]["question_number"]
        if quiz_game.questions_left():
            current_question = session["quiz_game"]["question_list"][question_number]["question"]
            current_answers = session["quiz_game"]["question_list"][question_number]["answers"]
            current_user_answers = session["quiz_game"]["user_answers"]
            current_user_score = session["quiz_game"]["score"]
            questions_left = True
        else:
            # Case when there are no more questions left
            current_question = "Quiz Finished"
            current_answers = []
            current_user_answers = session["quiz_game"]["user_answers"]
            current_user_score = session["quiz_game"]["score"]
            questions_left = False

    if not questions_left:
        session["user_score"] = current_user_score
        session["user_answers"] = current_user_answers
        return redirect(url_for("score.score"))


    return render_template("play_quiz.html",
                           form=form,
                           questions=quiz_questions,
                           current_question=current_question,
                           question_number=question_number,
                           current_answers=current_answers,
                           current_user_answers=current_user_answers,
                           current_user_score=current_user_score,
                           questions_left=questions_left)


@main_bp.route("/how_to_play")
def how_to_play():
    """Route for the rules of the game"""
    return render_template("how_to_play.html")


@main_bp.route("/leaderboard_main")
def leaderboard():
    """Route for Leaderboard"""
    leaderboard_instance = Leaderboard(conn)
    scores = leaderboard_instance.display_top_scores()
    form = LeaderboardForm
    return render_template("leaderboard.html", form=form, scores=scores)


# @main_bp.route("/setup")
# def setup():
#     """Route for the quiz setup"""
#     return render_template("quiz_setup.html")
