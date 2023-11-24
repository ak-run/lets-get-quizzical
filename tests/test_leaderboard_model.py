import unittest
from unittest.mock import MagicMock
from models.db_connection_model import DatabaseConnection
from models.leaderboard_model import DbConnectionError, Leaderboard


class TestLeaderBoard(unittest.TestCase):
    """
    Test cases for the LeaderBoard class.
    """

    def setUp(self):
        """
        Set up the test by creating a mock DatabaseConnection.
        """
        self.mock_db_connection = MagicMock(spec=DatabaseConnection)
        self.mock_leaderboard = Leaderboard(self.mock_db_connection)

    def test_valid_display_top_scores(self):
        """
        Test the display_top_scores method with valid input.
        The method should return top scores from the database.
        """
        # Values for the Mock
        self.mock_leaderboard.display_top10_sql_query = "SELECT nickname, score FROM top_scores_view;"
        self.mock_db_connection.get_connection_to_db.return_value.cursor.return_value.fetchall.return_value = \
            [("Player1", 100), ("Player2", 90)]
        result = self.mock_leaderboard.display_top_scores()
        self.assertEqual(result, [("Player1", 100), ("Player2", 90)])

    def test_valid_add_user_score(self):
        """
        Test the add_user_score method with valid input.
        The method should add a user score to the database and return a success status code, 200
        """
        # Values for the Mock
        self.mock_leaderboard.add_user_score_sql_query = "CALL AddUserScore('TestUser', 10);"
        self.mock_db_connection.get_connection_to_db.return_value.cursor.return_value.fetchall.return_value = None

        result, status_code = self.mock_leaderboard.add_user_score()

        self.assertEqual(status_code, 200)

    def test_execute_sql_query_with_exception(self):
        """
        Test the execute_sql_query method when an exception is raised.
        The method should handle the exception and raise a DbConnectionError.
        This method is used by both add_user_score and display_top_scores methods
        """
        # Values for the Mock
        self.mock_leaderboard.display_top10_sql_query = "CALL AddUserScore('User', 10);"
        self.mock_db_connection.get_connection_to_db.return_value.cursor.return_value.execute.side_effect = \
            Exception("Test error")

        with self.assertRaises(DbConnectionError):
            self.mock_leaderboard.add_user_score()


if __name__ == '__main__':
    unittest.main()
