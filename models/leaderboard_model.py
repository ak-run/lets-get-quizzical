import mysql.connector


class DbConnectionError(Exception):
    pass


class Leaderboard:
    """Class to add new users' score and then display top scores on Leadaerboard"""
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self._display_top10_sql_query = "SELECT position, nickname, score FROM top_scores_view;"
        self._add_user_score_sql_query = "CALL AddUserScore('%s', %s)"

    def execute_sql_query(self, query, fetch_results=False):
        """Method to execute an SQL query"""
        try:
            with self.db_connection.get_connection_to_db() as connection:
                cur = connection.cursor()
                cur.execute(query)

                if fetch_results:
                    result = cur.fetchall()
                else:
                    result = None

                connection.commit()
                return result

        except Exception as e:
            connection.rollback()
            raise DbConnectionError(f"Failed to execute query. MySQL Connector Error: {e}")

    def display_top_scores(self):
        """Method to display leaderboard of top scores"""
        return self.execute_sql_query(self._display_top10_sql_query, fetch_results=True)

    def add_user_score(self, nickname, score):
        """Method to add score to database"""
        formatted_query = self._add_user_score_sql_query % (nickname, score)
        result = self.execute_sql_query(formatted_query)
        return result, 200
