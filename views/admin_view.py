class AdminView:
    def display_users(self, users):
        """Display a list of all users."""
        if not users:
            print("No users found.")
            return
        for user in users:
            print(f"ID: {user['user_id']}, Username: {user['username']}")

    def confirm_deletion(self):
        """Ask for confirmation before deleting a user."""
        while True:
            confirmation = input("Are you sure you want to delete this user? (yes/no): ").lower()
            if confirmation in ['yes', 'no']:
                return confirmation == 'yes'
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    def show_deletion_success(self):
        """Display a success message for user deletion."""
        print("User deleted successfully.")

    def show_car_addition_success(self):
        """Display a success message for car addition."""
        print("Car added successfully.")

    def show_car_update_success(self):
        """Display a success message for car update."""
        print("Car updated successfully.")

    def show_car_deletion_success(self):
        """Display a success message for car deletion."""
        print("Car deleted successfully.")

    def show_rental_approval_success(self, rental):
        """Display a success message for rental approval."""
        print(f"Rental request {rental['id']} approved successfully.")

    def show_rental_rejection_success(self, rental):
        """Display a success message for rental rejection."""
        print(f"Rental request {rental['id']} rejected successfully.")

    def show_error(self, message):
        """Display an error message."""
        print(f"Error: {message}")

    def get_login_credentials(self):
        """Prompt the admin for their username and password."""
        while True:
            username = input("Enter admin username: ").strip()
            password = input("Enter admin password: ").strip()
            if username and password:
                return username, password
            else:
                print("Username and password cannot be empty.")

    def show_login_success(self, admin):
        """Display a success message when login is successful."""
        print("Admin login successfully.")

    def show_login_failure(self):
        """Display a message when login fails."""
        print("Admin login failed: Invalid credentials.")

    def display_cars(self, cars):
        """Display a list of all cars."""
        if not cars:
            print("No cars found.")
            return
        for car in cars:
            print(f"ID: {car['id']}, Model: {car['model']}, Make: {car['make']}, Year: {car['year']}")

    def display_rentals(self, rentals):
        """Display a list of all rentals."""
        if not rentals:
            print("No rentals found.")
            return
        for rental in rentals:
            print(f"ID: {rental['id']}, Car ID: {rental['car_id']}, User ID: {rental['user_id']}, Rental Period: {rental['rental_period']}")

    def display_rental(self, rental):
        """Display a single rental record."""
        print(f"ID: {rental['id']}, Car ID: {rental['car_id']}, User ID: {rental['user_id']}, Rental Period: {rental['rental_period']}")

    def get_rental_action(self):
        """Prompt for the action to take on a rental request."""
        while True:
            action = input("Enter action for rental (approve/reject): ").strip().lower()
            if action in ['approve', 'reject']:
                return action
            else:
                print("Invalid action. Please enter 'approve' or 'reject'.")
