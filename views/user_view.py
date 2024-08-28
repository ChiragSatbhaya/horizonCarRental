class UserView:
    def get_registration_details(self):
        """Prompt for user registration details."""
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        return username, password

    def get_login_details(self):
        """Prompt for user login details."""
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        return username, password

    def get_update_details(self):
        """Prompt for user update details."""
        username = input("Enter a new username: ")
        password = input("Enter a new password: ")
        return username, password

    def confirm_deletion(self):
        """Ask for confirmation before deleting a user."""
        confirmation = input("Are you sure you want to delete your account? (yes/no): ")
        return confirmation.lower() == 'yes'

    def show_registration_success(self):
        """Display a success message for registration."""
        print("Registration successful.")

    def show_login_success(self, user):
        """Display a success message for login."""
        print(f"Login successful. Welcome, {user['username']}!")

    def show_login_failure(self):
        """Display a failure message for login."""
        print("Login failed. Please check your username and password.")

    def show_update_success(self):
        """Display a success message for user update."""
        print("User details updated successfully.")

    def show_deletion_success(self):
        """Display a success message for account deletion."""
        print("Account deleted successfully.")
