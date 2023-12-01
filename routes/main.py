from flask import Blueprint, render_template
from models.stopwatch_model import StopWatch

# blueprint for main page
main_bp = Blueprint("/", __name__, static_folder="static", template_folder="templates")



import time
# def displayMe():
#     print('let\'s proceed to the next question..')
#
# class StopWatch:
#     def __init__(self, start, end):
#         self.value = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.value < self.end:
#             raise StopIteration
#
#         current = self.value
#         time.sleep(1)
#         self.value = self.value - 1
#
#         if current == 0:
#             print('hej, time is up')
#             displayMe()
#         return current
# numbers = StopWatch(60,0)
# for n in numbers:
#     print(n)
#


@main_bp.route("/")
def main():
    """Route for main page"""
    return render_template("index.html")

@main_bp.route("/single")
def single():
    """Route for the single player page"""
    return render_template("single.html")
    

@main_bp.route("/how_to_play")
def how_to_play():
    """Route for the rules of the game"""
    return render_template("how_to_play.html")

@main_bp.route("/leaderboard")
def leaderboard():
    """Route for the leader board"""
    return render_template("leaderboard.html")