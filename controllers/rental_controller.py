from models.crud_operations import CrudOperations
from models.car import Car
from views.rental_view import RentalView
from models.rental import Rental

class RentalController:
    def __init__(self, db):
        self.car_model = Car(db)
        self.rental_model = Rental(db)
        self.db = db
        self.crud = CrudOperations(db)
        self.rental_view = RentalView()

    def view_available_cars(self):
        """Display all cars available for rental."""
        cars = self.car_model.get_available_cars()
        self.rental_view.display_cars(cars)

    def book_car(self, user):
        """Allow a user to book a car."""
        available_cars = self.car_model.get_available_cars()
        if not available_cars:
            print("No cars available to book.")
            return

        rental_details = self.rental_view.get_rental_details(available_cars)
        if rental_details is None:
            print("Invalid rental details.")
            return

        # Extract details from the rental_details
        car_id, start_date, end_date, total_cost = rental_details

        # Use the user ID from the logged-in user object
        user_id = user['id']

        print(
            f"Entered details: user_id={user_id}, car_id={car_id}, start_date={start_date}, end_date={end_date}, total_cost={total_cost}")  # Debug print

        if not car_id or not start_date or not end_date or total_cost is None:
            print("Invalid rental details.")
            return

        if not self.validate_rental_dates(start_date, end_date):
            print("Invalid rental dates.")
            return

        # Proceed with booking
        self.rental_model.create_rental(user_id, car_id, start_date, end_date, total_cost)
        self.rental_view.show_booking_success()

    def view_user_bookings(self, user):
        """Display bookings made by a specific user."""
        user['id'] = user.get('id')
        if user['id'] is None:
            print("User ID not found.")
            return
        bookings = self.rental_model.get_user_rentals(user['id'])
        self.rental_view.display_rentals(bookings)

    def view_all_rentals(self):
        """Display all rental records."""
        rentals = self.rental_model.get_all_rentals()
        self.rental_view.display_rentals(rentals)

    def manage_rentals(self):
        """Approve or reject rental requests."""
        rentals = self.rental_model.get_all_rentals()
        if not rentals:
            print("No rentals found.")
            return

        for rental in rentals:
            if rental['status'] == 'Pending':
                self.rental_view.display_rentals([rental])
                action = input("Enter action (approve/reject): ")
                if action == 'approve':
                    self.rental_model.approve_rental(rental['id'])
                    self.rental_view.show_approval_success()
                elif action == 'reject':
                    self.rental_model.reject_rental(rental['id'])
                    self.rental_view.show_rejection_success()
                else:
                    print("Invalid action. Please try again.")

    def calculate_total_cost(self, car_id, rental_period):
        """Calculate the total cost for renting a car."""
        car = self.car_model.get_car_by_id(car_id)
        if car and 'daily_rate' in car:
            daily_rate = car['daily_rate']
            return daily_rate * rental_period
        else:
            print(f"Error: 'daily_rate' not found for car ID {car_id}.")
            return 0

    def validate_rental_dates(self, start_date, end_date):
        """Validate rental dates."""
        from datetime import datetime
        try:
            start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
            end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
            return start_date_obj < end_date_obj
        except ValueError:
            print("Error: Dates must be in the format YYYY-MM-DD.")
            return False