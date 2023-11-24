
class ScoreBoard:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def save_score_in_db(self, user_name, score, max_score):
        # Save individual score in the database
        pass

    def display_scoreboard(self):
        # Display scoreboard, probably we can create a view in DB and get data from that
        pass
