from flask import Blueprint, render_template

leaderboard_bp = Blueprint("leaderboard", __name__, static_folder="static", template_folder="templates")


@leaderboard_bp.route("/")
def leaderboard():
    """Route for Leaderboard"""
    return render_template("leaderboard.html")
