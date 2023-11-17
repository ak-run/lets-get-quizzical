from flask import Flask, render_template
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField


app = Flask(__name__)


if __name__ == '__main__':
    app.run()