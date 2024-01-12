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
        with unittest.mock.patch.object(self.mock_leaderboard, 'execute_sql_query',
                                        return_value=[("Player1", 100), ("Player2", 90)]):
            result = self.mock_leaderboard.display_top_scores()

        # Assert that the result is what you expect
        self.assertEqual(result, [("Player1", 100), ("Player2", 90)])

    def test_valid_add_user_score(self):
        """
        Test the add_user_score method with valid input.
        The method should add a user score to the database and return a success status code, 200
        """
        result, status_code = self.mock_leaderboard.add_user_score("avatar1.png", "TestUser", 10)
        self.assertEqual(status_code, 200)

    def test_execute_sql_query_with_value_error(self):
        """
        Test the execute_sql_query method when a ValueError is raised.
        The method should handle the exception and raise a ValueError.
        This method is used by both add_user_score and display_top_scores methods
        """
        with unittest.mock.patch.object(Leaderboard, 'execute_sql_query', side_effect=DbConnectionError("Test error")):
            with self.assertRaises(ValueError):
                self.mock_leaderboard.add_user_score("avatar", "TestUser", 11)


if __name__ == '__main__':
    unittest.main()
