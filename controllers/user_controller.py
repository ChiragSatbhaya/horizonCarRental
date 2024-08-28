from models.user import User
from views.user_view import UserView
from models.crud_operations import CrudOperations

class UserController:
    def __init__(self, db):
        self.user_model = User(db)
        self.user_view = UserView()
        self.crud_operations = CrudOperations(db)

    def register(self):
        """Register a new user."""
        username, password = self.user_view.get_registration_details()
        role = "user"
        self.user_model.register(username, password, role)
        self.user_view.show_registration_success()

    def login(self):
        """Authenticate user login."""
        username, password = self.user_view.get_login_details()
        user = self.user_model.authenticate(username, password)
        if user:
            self.user_view.show_login_success(user)
            return user
        else:
            self.user_view.show_login_failure()
            return None

    def update(self, user_id):
        """Update user details."""
        username, password = self.user_view.get_update_details()
        self.user_model.update(user_id, username, password)
        self.user_view.show_update_success()

    def delete(self, user_id):
        """Delete a user."""
        confirmation = self.user_view.confirm_deletion()
        if confirmation:
            self.user_model.delete(user_id)
            self.user_view.show_deletion_success()

    def view_bookings(self, user_id):
        """Allow users to view their own bookings."""
        bookings = self.crud_operations.get_user_bookings(user_id)
        self.user_view.display_bookings(bookings)

    def book_car(self, user_id, car_id, rental_period):
        """Allow users to book a car."""
        booking_details = {
            'user_id': user_id,
            'car_id': car_id,
            'rental_period': rental_period
        }
        success = self.crud_operations.book_car(booking_details)
        if success:
            self.user_view.show_booking_success()
        else:
            self.user_view.show_booking_failure()

    def cancel_booking(self, booking_id):
        """Allow users to cancel a booking."""
        confirmation = self.user_view.confirm_cancellation()
        if confirmation:
            self.crud_operations.cancel_booking(booking_id)
            self.user_view.show_cancellation_success()

