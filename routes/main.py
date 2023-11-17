from flask import Blueprint, render_template

# blueprint for main page
main_bp = Blueprint("/", __name__)


@main_bp.route("/")
def main():
    """Route for main page"""
    return render_template("index.html")
