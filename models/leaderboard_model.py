import mysql.connector


class DbConnectionError(Exception):
    pass


class Leaderboard:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self._display_top10_sql_query = "SELECT position, nickname, score FROM top_scores_view;"
        self._add_user_score_sql_query = "CALL AddUserScore('%s', %s)"
    #
    # @property
    # def add_user_score_sql_query(self):
    #     print("To set this query pass username and score")
    #
    # @add_user_score_sql_query.setter
    # def add_user_score_sql_query(self, nickname, score):
    #     self._add_user_score_sql_query = "CALL AddUserScore('%s', %s)" % (nickname, score)

    def execute_sql_query(self, query, *params, fetch_results=False):
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
        except mysql.connector.Error as e:
            connection.rollback()
            raise DbConnectionError(f"Failed to execute query. MySQL Connector Error: {e}")

    def display_top_scores(self):
        return self.execute_sql_query(self._display_top10_sql_query, fetch_results=True)

    def add_user_score(self, nickname, score):
        query = "CALL AddUserScore(%s, %s)"
        result = self.execute_sql_query(query, nickname, score)
        return result
