from flask import Blueprint, render_template, request, redirect, url_for, session
from routes.flask_forms import ScoreForm
from models.db_connection_model import DatabaseConnection, config
from models.leaderboard_model import Leaderboard

score_bp = Blueprint("score", __name__, static_folder="static", template_folder="templates")

conn = DatabaseConnection(config)
conn.get_connection_to_db()


@score_bp.route("/", methods=["GET", "POST"])
def score():
    """Route for displaying user score and adding it to database"""
    form = ScoreForm()

    if request.method == "POST" and form.validate_on_submit():
        avatar = session["avatar"]
        nickname = session['nickname']
        score = session["user_score"]

        leaderboard_instance = Leaderboard(conn)
        # Execute the query to add the user score to the database
        leaderboard_instance.add_user_score(avatar, nickname, score)
        session.clear()
        if not session:
            print("session is clear")

        # Redirect back to the leaderboard after adding the score
        return redirect(url_for("/.leaderboard"))

    return render_template("score.html",
                           form=form,
                           user_score=session.get("user_score", None),
                           user_answers=session.get("user_answers"))
