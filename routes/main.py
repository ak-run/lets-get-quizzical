from flask import Blueprint, render_template

# blueprint for main page
main_bp = Blueprint("/", __name__, static_folder="static", template_folder="templates")

@main_bp.route("/")
def main():
    """Route for main page"""
    return render_template("index.html")

@main_bp.route("/single.html")
def single():
    """Route for the single player page"""
    return render_template("single.html")
    z