from models.user import User
from views.admin_view import AdminView
from models.crud_operations import CrudOperations

class AdminController:
    def __init__(self, db):
        self.user_model = User(db)
        self.admin_view = AdminView()
        self.crud_operations = CrudOperations(db)

    def login(self):
        """Admin login function."""
        username, password = self.admin_view.get_login_credentials()
        admin = self.user_model.admin_login(username, password)
        if admin:
            self.admin_view.show_login_success(admin)
            return admin
        else:
            self.admin_view.show_login_failure()
            return None

    def view_all_users(self):
        """View all users in the system."""
        users = self.user_model.get_all_users()
        self.admin_view.display_users(users)

    def delete_user(self, user_id):
        """Delete a user by user_id."""
        confirmation = self.admin_view.confirm_deletion()
        if confirmation:
            self.user_model.delete(user_id)
            self.admin_view.show_deletion_success()

    def add_car(self, car_details):
        """Add a new car to the system."""
        self.crud_operations.add_car(car_details)
        self.admin_view.show_car_addition_success()

    def update_car(self, car_id, updated_details):
        """Update an existing car's details."""
        self.crud_operations.update_car(car_id, updated_details)
        self.admin_view.show_car_update_success()

    def delete_car(self, car_id):
        """Delete a car from the system."""
        confirmation = self.admin_view.confirm_deletion()
        if confirmation:
            self.crud_operations.delete_car(car_id)
            self.admin_view.show_car_deletion_success()

    def view_all_cars(self):
        """View all cars in the system."""
        cars = self.crud_operations.get_all_cars()
        self.admin_view.display_cars(cars)

    def view_all_rentals(self):
        """View all rental records."""
        rentals = self.crud_operations.get_all_rentals()
        self.admin_view.display_rentals(rentals)

    def manage_rentals(self):
        """Approve or reject rental requests."""
        rentals = self.crud_operations.get_pending_rentals()
        for rental in rentals:
            self.admin_view.display_rental(rental)
            action = self.admin_view.get_rental_action()
            if action == 'approve':
                self.crud_operations.approve_rental(rental['id'])
                self.admin_view.show_rental_approval_success(rental)
            elif action == 'reject':
                self.crud_operations.reject_rental(rental['id'])
                self.admin_view.show_rental_rejection_success(rental)
