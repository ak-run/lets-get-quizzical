# File with Flask Forms for Routes
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, StringField


class QuestionForm(FlaskForm):
    user_answer = RadioField('Answer', choices=[], coerce=int)

    submit = SubmitField("Submit")


class ProfileForm(FlaskForm):
    nickname = StringField('Nickname')
    submit = SubmitField('Start Quiz')


class LeaderboardForm(FlaskForm):
    """pass because there are no special fields in the Flask Form needed"""
    pass
