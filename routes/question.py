from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField


# blueprint for question
question_bp = Blueprint("question", __name__)


class QuestionForm(FlaskForm):
    submit = SubmitField("Submit")


@question_bp.route("/", methods=['GET', 'POST'])
def question():
    """Route for question"""
    form = QuestionForm()
    message = ""
    results = []
    return render_template("question.html", form=form, results=results, message=message)
