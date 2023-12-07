from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField

from models.question_model import QuizQuestions




# blueprint for question 
category_bp = Blueprint("category", __name__, static_folder="static", template_folder="templates")


class CategoryForm(FlaskForm):
    submit = SubmitField("Submit")


@category_bp.route("/", methods=['GET', 'POST'])
def category():
    """Route for question"""

    form = CategoryForm()
    quiz = QuizQuestions()
    # for categories in quiz.question_categories:
    #     return categories
        
    return render_template("category.html", form=form, cat=quiz.question_categories)



quiz = QuizQuestions()
for categories in quiz.question_categories:
    print(categories)

