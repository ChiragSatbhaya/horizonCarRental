class RentalView:
    def get_rental_details(self, available_cars):
        """Prompt for rental details including car selection."""
        car_id = input("Enter the car ID you want to rent: ")

        # Print available car IDs for debugging
        available_car_ids = [str(car['id']) for car in available_cars]
        print(f"Available car IDs: {available_car_ids}")

        # Check if car_id is in available_car_ids
        if car_id not in available_car_ids:
            print("Invalid car ID.")
            return None, None, None, None

        start_date = input("Enter rental start date (YYYY-MM-DD): ")
        end_date = input("Enter rental end date (YYYY-MM-DD): ")

        # Validate and calculate total cost
        from datetime import datetime
        try:
            start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
            end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            print("Error: Dates must be in the format YYYY-MM-DD.")
            return None, None, None, None

        rental_period = (end_date_obj - start_date_obj).days

        if rental_period <= 0:
            print("Rental period must be greater than zero.")
            return None, None, None, None

        car = next((car for car in available_cars if str(car['id']) == car_id), None)
        if car:
            daily_rate = car['daily_rate']
            total_cost = daily_rate * rental_period
        else:
            print("Error: Car not found.")
            return None, None, None, None

        return car_id, start_date, end_date, total_cost

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
