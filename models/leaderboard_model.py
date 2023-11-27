import mysql.connector


class DbConnectionError(Exception):
    pass


class Leaderboard:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self._display_top10_sql_query = "SELECT position, nickname, score FROM top_scores_view;"
        self._add_user_score_sql_query = "CALL AddUserScore('%s', %s)"

    def execute_sql_query(self, query, *params, fetch_results=False):
        """Method to execute an SQL query. Optional **param are for queries requiring values being passed"""
        try:
            with self.db_connection.get_connection_to_db() as connection:
                cur = connection.cursor()
                if not params:
                    cur.execute(query)
                else:
                    cur.execute(query, params)

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
        result = self.execute_sql_query(self._add_user_score_sql_query, nickname, score)
        return result, 200
