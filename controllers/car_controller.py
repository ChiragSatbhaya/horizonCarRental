from models.car import Car
from views.car_view import CarView

class CarController:
    def __init__(self, db):
        self.car_model = Car(db)
        self.car_view = CarView()

    def add_car(self):
        """Add a new car to the system."""
        car_details = self.car_view.get_car_details()
        self.car_model.add_car(*car_details)
        self.car_view.show_add_success()

    def update_car(self, car_id):
        """Update details of an existing car."""
        car_details = self.car_view.get_car_details()
        self.car_model.update_car(car_id, *car_details)
        self.car_view.show_update_success()

    def delete_car(self, car_id):
        """Delete a car from the system."""
        confirmation = self.car_view.confirm_deletion()
        if confirmation:
            self.car_model.delete_car(car_id)
            self.car_view.show_deletion_success()

    def view_available_cars(self):
        """Display all available cars."""
        cars = self.car_model.get_available_cars()
        self.car_view.display_cars(cars)

    def view_all_cars(self):
        """Display all cars in the system, regardless of availability."""
        cars = self.car_model.get_all_cars()
        self.car_view.display_cars(cars)

    def recommend_cars(self, user):
        """Recommend cars based on user preferences."""
        preferences = self.car_view.get_user_preferences()
        recommended_cars = self.car_model.find_cars_by_preferences(preferences)
        self.car_view.display_cars(recommended_cars)