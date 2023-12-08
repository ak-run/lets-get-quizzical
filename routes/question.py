# from flask import Blueprint, render_template, request, session
# from flask_wtf import FlaskForm
# from wtforms import SubmitField, StringField
# from models.question_model import QuizQuestions
#
#
# # blueprint for question
# question_bp = Blueprint("question", __name__, static_folder="static", template_folder="templates")
#
#
# class QuestionForm(FlaskForm):
#     user_answer = StringField("Answer")
#     submit = SubmitField("Submit")
#
#
# @question_bp.route("/single", methods=['GET', 'POST'])
# def single(category):
#     if request.method == 'POST':
#         session.permanent = True
#     quiz = QuizQuestions()
#     questions = quiz.create_quiz_question_dict()
#     quiz.url = category
#     session['quiz_questions'] = questions
#
#     return render_template("single.html", questions=questions)