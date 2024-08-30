from datetime import datetime

class RentalView:
    def get_rental_details(self, available_cars):
        """Prompt for rental details including car selection."""
        while True:
            car_id = input("Enter the car ID you want to rent: ").strip()
            if not car_id.isdigit() or car_id not in [str(car['id']) for car in available_cars]:
                print("Invalid car ID. Please select a valid car ID from the list.")
                continue

            start_date = input("Enter rental start date (YYYY-MM-DD): ").strip()
            end_date = input("Enter rental end date (YYYY-MM-DD): ").strip()

            try:
                start_date_obj = datetime.strptime(start_date, '%Y-%m-%d').date()
                end_date_obj = datetime.strptime(end_date, '%Y-%m-%d').date()
                today = datetime.now().date()
                if start_date_obj <= today:
                    print("Error: Start date must be after today's date.")
                    continue
                if start_date_obj >= end_date_obj:
                    print("Error: Start date must be before end date.")
                    continue
                rental_period = (end_date_obj - start_date_obj).days
                if rental_period <= 0:
                    print("Error: Rental period must be greater than zero.")
                    continue

                car = next((car for car in available_cars if str(car['id']) == car_id), None)
                if car:
                    total_cost = car['daily_rate'] * rental_period
                    return car_id, start_date, end_date, total_cost
                else:
                    print("Error: Car not found.")
            except ValueError:
                print("Error: Dates must be in the format YYYY-MM-DD.")

    def display_cars(self, cars):
        """Display a list of available cars."""
        if not cars:
            print("No cars available.")
            return
        for car in cars:
            print(f"ID: {car['id']}, Make: {car['make']}, Model: {car['model']}, Year: {car['year']}, "
                  f"Mileage: {car['mileage']}, Available: {car['available_now']}, "
                  f"Min Rent Period: {car['min_rent_period']} days, Max Rent Period: {car['max_rent_period']} days")

    def display_rentals(self, rentals):
        """Display a list of rentals."""
        if not rentals:
            print("No rentals found.")
            return
        for rental in rentals:
            print(f"Rental ID: {rental['id']}, User ID: {rental['user_id']}, Car ID: {rental['car_id']}, "
                  f"Start Date: {rental['start_date']}, End Date: {rental['end_date']}, "
                  f"Total Cost: {rental['total_cost']}, Status: {rental['status']}")

    def confirm_cancellation(self):
        """Ask for confirmation before canceling a rental."""
        confirmation = input("Are you sure you want to cancel this rental? (yes/no): ")
        return confirmation.lower() == 'yes'

    def show_booking_success(self):
        """Display a success message for booking a car."""
        print("Car rental booked successfully.")

    def show_cancellation_success(self):
        """Display a success message for canceling a rental."""
        print("Car rental canceled successfully.")

    def show_approval_success(self):
        """Display a success message for approving a rental."""
        print("Car rental approved successfully.")

    def show_rejection_success(self):
        """Display a success message for rejecting a rental."""
        print("Car rental rejected.")