import json
import mysql.connector
import os

# Get the absolute path of the configuration file
config_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../config/config.json"))

# Read the configuration from the JSON file
with open(config_file_path) as config_file:
    config = json.load(config_file)


class DatabaseConnection:
    """
    Class to connect to a database using a configuration file.
    """
    def __init__(self, config):
        """
        Initialize the DatabaseConnection object with the provided configuration.
        Parameter: config (dict): A dictionary containing the database configuration.
        Expected keys: 'host', 'user', 'password', 'database_name'.
        """
        self.db_config = config['database']
        self.db_host = self.db_config['host']
        self.db_user = self.db_config['user']
        self.db_password = self.db_config['password']
        self.db_name = self.db_config['database_name']
        self.connection = None

    def get_connection_to_db(self):
        """
        Establish a connection to a MySQL database.
        Returns: A MySQL database connection object.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.db_host,
                user=self.db_user,
                password=self.db_password,
                database=self.db_name
            )
            return self.connection

        except mysql.connector.Error as err:
            print(f"Error connecting to the database: {err}")
            raise

    def conn_close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            self.connection = None
