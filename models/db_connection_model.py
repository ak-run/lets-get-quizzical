import mysql.connector


class DatabaseConnection:
    """
    Class to connect to a database using a configuration file.
    Parameter: config (dict): A dictionary containing the database configuration.
                      Expected keys: 'host', 'user', 'password', 'database_name'.
    Methods:
        get_connection_to_db(): establishes a connection to a MySQL database.
        conn_close(): Closes the database connection.
    """
    def __init__(self, config):
        self.db_config = config['database']
        self.db_host = self.db_config['host']
        self.db_user = self.db_config['user']
        self.db_password = self.db_config['password']
        self.db_name = self.db_config['database_name']
        self.connection = None

    def get_connection_to_db(self):
        """Establish a connection to a MySQL database."""
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