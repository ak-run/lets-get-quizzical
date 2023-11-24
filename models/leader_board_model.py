from models.db_connection_model import DatabaseConnection
from pprint import pprint
import json


class DbConnectionError(Exception):
    pass


class LeaderBoard:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self._display_top10_sql_query = ""
        self._add_user_score_sql_query = ""

    @property
    def display_top10_sql_query(self):
        return self._display_top10_sql_query

    @display_top10_sql_query.setter
    def display_top10_sql_query(self, query):
        self._display_top10_sql_query = query

    @property
    def add_user_score_sql_query(self):
        return self._add_user_score_sql_query

    @add_user_score_sql_query.setter
    def add_user_score_sql_query(self, query):
        self._add_user_score_sql_query = query

    def execute_sql_query(self, query):
        try:
            connection = self.db_connection.get_connection_to_db()
            cur = connection.cursor()
            cur.execute(query)
            result = cur.fetchall()
            cur.close()
            return result
        except Exception as e:
            raise DbConnectionError(f"Failed to execute query. Exception: {e}")
        finally:
            connection.close()

    def display_top_scores(self):
        return self.execute_sql_query(self._display_top10_sql_query)

    def add_user_score(self):
        return self.execute_sql_query(self._add_user_score_sql_query)


with open('../config.json') as config_file:
    config = json.load(config_file)

conn = DatabaseConnection(config)
conn.get_connection_to_db()
leaderboard = LeaderBoard(conn)
leaderboard.display_top10_sql_query = "SELECT nickname, score FROM top_scores_view;"
pprint(leaderboard.display_top_scores())
