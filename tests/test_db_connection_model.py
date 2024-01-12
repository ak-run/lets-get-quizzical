import unittest
import json
import mysql.connector
from models.db_connection_model import DatabaseConnection, config_file_path

with open(config_file_path) as config_file:
    config = json.load(config_file)


class TestDatabaseConnection(unittest.TestCase):
    """Testing the db_connection_model to check for successful connection to SQL"""

    def setUp(self):
        """Get a new connection for each test"""
        self.connection = DatabaseConnection(config).get_connection_to_db()

    def tearDown(self):
        """Close the connection after each test"""
        self.connection.close()

    def test_valid_get_connection_to_db(self):
        """Test if the get_connection_to_db method returns a valid connection"""
        self.assertIsInstance(self.connection, mysql.connector.MySQLConnection)

    def test_invalid_get_connection_to_db(self):
        """Test if the get_connection_to_db method raises an exception for invalid configuration"""
        invalid_config = {"database": {
            "host": "invalid_host",
            "user": "invalid_user",
            "password": "invalid_password",
            "database_name": "invalid_name"
        }}

        with self.assertRaises(mysql.connector.Error):
            DatabaseConnection(invalid_config).get_connection_to_db()


if __name__ == '__main__':
    unittest.main()
