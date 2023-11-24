import json
from flask import Blueprint, render_template
from models.db_connection_model import DatabaseConnection, config
from models.leaderboard_model import Leaderboard

leaderboard_bp = Blueprint("leaderboard", __name__, static_folder="static", template_folder="templates")

conn = DatabaseConnection(config)
conn.get_connection_to_db()


@leaderboard_bp.route("/")
def leaderboard():
    """Route for Leaderboard"""
    leaderboard_instance = Leaderboard(conn)
    leaderboard_instance.display_top10_sql_query = "SELECT nickname, score FROM top_scores_view;"
    return render_template("leaderboard.html", leaderboard=leaderboard_instance)
