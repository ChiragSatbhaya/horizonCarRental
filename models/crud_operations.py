import mysql.connector

class CrudOperations:
    def __init__(self, db):
        self.db = db

    def execute_query(self, query, data=None):
        """Execute a query with optional data."""
        cursor = self.db.get_cursor(dictionary=True)
        try:
            cursor.execute(query, data)
            self.db.commit()
            return cursor
        except mysql.connector.Error as e:
            print(f"Error executing query: {e}")
        finally:
            cursor.close()

    def fetchone(self, query, data=None):
        """Fetch one record from the database."""
        cursor = self.db.get_cursor(dictionary=True)
        try:
            cursor.execute(query, data)
            result = cursor.fetchone()
            return result
        except mysql.connector.Error as e:
            print(f"Error fetching data: {e}")
            return None
        finally:
            cursor.close()

    def fetchall(self, query, data=None):
        """Fetch all records from the database."""
        cursor = self.db.get_cursor(dictionary=True)
        try:
            cursor.execute(query, data)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as e:
            print(f"Error fetching data: {e}")
            return []
        finally:
            cursor.close()

    def read_user(self, username):
        query = "SELECT username, password, role FROM users WHERE username=%s"
        result = self.db.fetchone(query, (username,))
        if result:
            return {
                'username': result[0],
                'password': result[1],
                'role': result[2]
            }
        return None

    def read_user_by_id(self, user_id):
        """Read user details by user ID."""
        query = "SELECT * FROM users WHERE user_id = %s"
        result = self.fetchone(query, (user_id,))
        return result if result else None

    def read_all_users(self):
        """Read all users."""
        query = "SELECT * FROM users"
        return self.fetchall(query)

    def create_user(self, user_data):
        """Create a new user."""
        query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
        self.execute_query(query, user_data)

    def update_user(self, user_data):
        """Update user details."""
        query = "UPDATE users SET username = %s, password = %s WHERE user_id = %s"
        self.execute_query(query, user_data)

    def delete_user(self, user_id):
        """Delete a user by ID."""
        query = "DELETE FROM users WHERE user_id = %s"
        self.execute_query(query, (user_id,))

    def add_car(self, car_details):
        """Add a new car."""
        query = "INSERT INTO cars (model, make, year) VALUES (%s, %s, %s)"
        self.execute_query(query, car_details)

    def update_car(self, car_id, updated_details):
        """Update car details."""
        query = "UPDATE cars SET model = %s, make = %s, year = %s WHERE id = %s"
        self.execute_query(query, (*updated_details, car_id))

    def delete_car(self, car_id):
        """Delete a car by ID."""
        query = "DELETE FROM cars WHERE id = %s"
        self.execute_query(query, (car_id,))

    def get_all_cars(self):
        """Retrieve all cars."""
        query = "SELECT * FROM cars"
        return self.fetchall(query)

    def get_all_rentals(self):
        """Retrieve all rentals."""
        query = "SELECT * FROM rentals"
        return self.fetchall(query)

    def get_pending_rentals(self):
        """Retrieve all pending rentals."""
        query = "SELECT * FROM rentals WHERE status = 'pending'"
        return self.fetchall(query)

    def approve_rental(self, rental_id):
        """Approve a rental request."""
        query = "UPDATE rentals SET status = 'approved' WHERE id = %s"
        self.execute_query(query, (rental_id,))

    def reject_rental(self, rental_id):
        """Reject a rental request."""
        query = "UPDATE rentals SET status = 'rejected' WHERE id = %s"
        self.execute_query(query, (rental_id,))
