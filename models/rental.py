from models.crud_operations import CrudOperations

class Rental:
    def __init__(self, db):
        self.crud = CrudOperations(db)

    def create_rental(self, user_id, car_id, start_date, end_date, total_cost):
        """Creates a new rental record."""
        rental_data = (user_id, car_id, start_date, end_date, total_cost, 'Pending')
        try:
            query = """
                INSERT INTO rentals (user_id, car_id, start_date, end_date, total_cost, status)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            self.crud.execute_query(query, rental_data)
            print("Rental created successfully.")
        except Exception as e:
            print(f"Error creating rental: {e}")

    def get_user_rentals(self, user_id):
        """Retrieves all rentals for a specific user."""
        query = "SELECT * FROM rentals WHERE user_id = %s"
        try:
            return self.crud.db.fetchall(query, (user_id,), dictionary=True)
        except Exception as e:
            print(f"Error fetching user rentals: {e}")
            return []

    def get_all_rentals(self):
        """Retrieves all rental records."""
        query = "SELECT * FROM rentals"
        try:
            return self.crud.db.fetchall(query, dictionary=True)
        except Exception as e:
            print(f"Error fetching all rentals: {e}")
            return []

    def approve_rental(self, rental_id):
        """Approves a rental request."""
        query = "UPDATE rentals SET status = 'Approved' WHERE id = %s"
        try:
            self.crud.db.execute_query(query, (rental_id,))
            print(f"Rental {rental_id} approved successfully.")
        except Exception as e:
            print(f"Error approving rental: {e}")

    def reject_rental(self, rental_id):
        """Rejects a rental request."""
        query = "UPDATE rentals SET status = 'Rejected' WHERE id = %s"
        try:
            self.crud.db.execute_query(query, (rental_id,))
            print(f"Rental {rental_id} rejected successfully.")
        except Exception as e:
            print(f"Error rejecting rental: {e}")