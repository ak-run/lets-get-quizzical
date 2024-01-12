# File with Flask Forms for Routes
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, StringField


class ProfileForm(FlaskForm):
    """
    Form for entering user profile information before starting the quiz.
    Attributes:
        nickname (StringField): Field for entering a user's nickname.
        submit (SubmitField): Button to start the quiz.
    """
    nickname = StringField('Nickname')
    submit = SubmitField('Start Quiz')


class QuestionForm(FlaskForm):
    """
    Form for submitting user answers to quiz questions.

    Attributes:
        user_answer (RadioField): Field for selecting a multiple-choice answer.
        submit (SubmitField): Button to submit the answer.
    """
    user_answer = RadioField('Answer', choices=[], coerce=int)
    submit = SubmitField("Submit")


class ScoreForm(FlaskForm):
    """
    Form for submitting user scores to the leaderboard.
    Attributes:
        submit (SubmitField): Button to submit the user's score.
    """
    submit = SubmitField('SUBMIT SCORE TO LEADERBOARD')


class LeaderboardForm(FlaskForm):
    """
    Placeholder form for the leaderboard page.
    This form does not have any specific fields, as it's used only for rendering the leaderboard page.
    """
    pass
