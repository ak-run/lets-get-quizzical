from flask import Blueprint, render_template, session, redirect, url_for, request
from routes.flask_forms import ProfileForm, QuestionForm, LeaderboardForm
from models.db_connection_model import DatabaseConnection, config
from models.leaderboard_model import Leaderboard
from models.question_model import QuizQuestions
from models.quizgame_model import QuizGame

# blueprint for main page
main_bp = Blueprint("/", __name__, static_folder="static", template_folder="templates")

conn = DatabaseConnection(config)
conn.get_connection_to_db()


@main_bp.route("/", methods=["GET", "POST"])
def main():
    """Main route for the application."""
    session.clear()
    form = ProfileForm()
    avatar_filenames = [f"{i}.png" for i in range(1, 13)]
    return render_template("index.html", form=form, avatar_filenames=avatar_filenames)


@main_bp.route("/start_quiz", methods=["POST"])
def start_quiz():
    """Route to start the quiz setup."""
    form = ProfileForm()
    if form.validate_on_submit():
        session['nickname'] = form.nickname.data
        session['avatar'] = request.form['avatar']
        # quiz = QuizQuestions()
        return render_template("quiz_setup.html", categories=QuizQuestions.question_categories)


@main_bp.route("/play_quiz", methods=["POST", "GET"])
def play_quiz():
    """Route for playing the quiz."""
    form = QuestionForm()

    # Check if the quiz_game is not already in the session
    if "quiz_game" not in session:
        # If not, retrieve the category
        category = request.args.get("category")
        # Create a QuizQuestions object and set its URL to the category, generate questions dictionary
        quiz_questions_obj = QuizQuestions()
        quiz_questions_obj.url = category
        quiz_questions = quiz_questions_obj.create_quiz_question_dict()
        # Create a QuizGame instance using the generated questions
        quiz_game = QuizGame(quiz_questions)
        # Store the quiz_game in the session as a dictionary
        session["quiz_game"] = quiz_game.to_dict()
    else:
        # If quiz_game is already in the session, retrieve its information
        quiz_questions = session["quiz_game"]["question_list"]
        quiz_game = QuizGame.from_dict(quiz_questions, session["quiz_game"])
        # Ask the current question and update the session with the game state
        quiz_game.ask_question(form.user_answer.data)
        session["quiz_game"] = quiz_game.to_dict()

    # Retrieve the current question number and bool informing if there are questions left in the quiz
    question_number = session["quiz_game"]["question_number"]
    questions_left = quiz_game.questions_left()

    #  Determine the details of the current question and user's progress
    if questions_left:
        current_question, current_answers, current_user_answers, current_user_score = (
            quiz_questions[question_number]["question"],
            quiz_questions[question_number]["answers"],
            session["quiz_game"]["user_answers"],
            session["quiz_game"]["score"]
        )
    else:
        # once quiz is finished store the score and user answers in session ready to display on the score page
        current_question, current_answers, current_user_answers, current_user_score = (
            "Quiz Finished",
            [],
            session["quiz_game"]["user_answers"],
            session["quiz_game"]["score"]
        )
        session["user_score"], session["user_answers"] = current_user_score, current_user_answers
        # Go to score page
        return redirect(url_for("score.score"))

    return render_template("play_quiz.html",
                           form=form,
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
    """Route for displaying the leaderboard."""
    leaderboard_instance = Leaderboard(conn)
    scores = leaderboard_instance.display_top_scores()
    form = LeaderboardForm
    return render_template("leaderboard.html", form=form, scores=scores)
