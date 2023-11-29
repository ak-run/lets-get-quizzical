from flask import Blueprint, render_template

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


@main_bp.route("/single.html")
def single():
    """Route for the single player page"""
    return render_template("single.html")
