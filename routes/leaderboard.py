import json
from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from models.db_connection_model import DatabaseConnection, config
from models.leaderboard_model import Leaderboard

leaderboard_bp = Blueprint("leaderboard", __name__, static_folder="static", template_folder="templates")

conn = DatabaseConnection(config)
conn.get_connection_to_db()


class LeaderboardForm(FlaskForm):
    pass


@leaderboard_bp.route("/")
def leaderboard():
    """Route for Leaderboard"""
    leaderboard_instance = Leaderboard(conn)
    leaderboard_instance.display_top10_sql_query = "SELECT position, nickname, score FROM top_scores_view;"
    scores = leaderboard_instance.display_top_scores()
    form = LeaderboardForm
    return render_template("leaderboard.html", form=form, scores=scores)

