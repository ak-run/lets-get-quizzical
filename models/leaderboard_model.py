class DbConnectionError(Exception):
    """Class for DB Connection Exception"""
    pass


class Leaderboard:
    """Class to add new users' score and then display top scores on Leaderboard"""
    def __init__(self, db_connection):
        """
        Initialize the Leaderboard object with a database connection.
        Parameters: db_connection: An instance of the DatabaseConnection class for database connectivity.
        """
        self.db_connection = db_connection
        self._display_top10_sql_query = "SELECT position, avatar, nickname, score FROM top_scores_view;"
        self._add_user_score_sql_query = "CALL AddUserScore('%s', '%s', '%s')"

    def execute_sql_query(self, query, fetch_results=False):
        """
        Method to execute an SQL query.
        Parameters: query: The SQL query to be executed.
                           fetch_results: Flag indicating whether to fetch results after executing the query.
        Returns: if fetch_results is True, returns a list of results; otherwise, returns None.
        Raises DbConnectionError: If there is an error executing the query.
        """
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
        """
        Method to display leaderboard of top scores
        Returns: a list of tuples containing top scores information.
        """
        return self.execute_sql_query(self._display_top10_sql_query, fetch_results=True)

    def add_user_score(self, avatar, nickname, score):
        """
        Method to add a user's score to the database.
        Parameters:
            avatar: the path to avatar of the user.
            nickname: the nickname of the user.
            score: the score of the user.
        Returns: result and status_code
        """
        # validate input parameters
        if not avatar or not nickname or not (1 <= len(nickname) <= 25) or not (0 <= score <= 10):
            raise ValueError("Invalid input parameters.")
        formatted_query = self._add_user_score_sql_query % (avatar, nickname, score)
        result = self.execute_sql_query(formatted_query)
        return result, 200
