import mysql.connector
from mysql.connector import Error
from config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

class Database:
    def __init__(self):
        self.connection = None
        self.connect()

    def connect(self):
        """Establish a connection to the MySQL database."""
        try:
            self.connection = mysql.connector.connect(
                host=DB_HOST,
                port=DB_PORT,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
            )
            if self.connection.is_connected():
                print("Connected to the database")
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            self.connection = None

    def close(self):
        """Close the database connection."""
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")

    def get_cursor(self, dictionary=False):
        """Get a new cursor from the connection."""
        if self.connection.is_connected():
            return self.connection.cursor(dictionary=dictionary)
        else:
            raise Error("Database connection is not established")

    def commit(self):
        """Commit the current transaction."""
        if self.connection.is_connected():
            self.connection.commit()

    def execute_query(self, query, params=None):
        """Execute a database query with optional parameters."""
        cursor = None
        try:
            cursor = self.get_cursor()
            cursor.execute(query, params)
            self.commit()
        except Error as e:
            print(f"Error executing query: {e}")
            self.close()
            self.connect()
        finally:
            if cursor:
                cursor.close()

    def fetchall(self, query, params=None, dictionary=False):
        """Fetch all results from a query."""
        cursor = None
        try:
            cursor = self.get_cursor(dictionary=dictionary)
            cursor.execute(query, params)
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error fetching data: {e}")
            return []
        finally:
            if cursor:
                cursor.close()

    def fetchone(self, query, params=None):
        """Fetch one result from a query."""
        cursor = None
        try:
            cursor = self.get_cursor()
            cursor.execute(query, params)
            result = cursor.fetchone()
            return result
        except Error as e:
            print(f"Error fetching data: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
