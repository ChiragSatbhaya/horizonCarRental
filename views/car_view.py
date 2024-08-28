class CarView:
    def get_car_details(self):
        """Prompt for car details to add or update a car."""
        make = input("Enter car make: ")
        model = input("Enter car model: ")
        year = input("Enter car year: ")
        mileage = input("Enter car mileage: ")
        available_now = input("Is the car available now? (yes/no): ").lower() == 'yes'
        min_rent_period = int(input("Enter minimum rent period (in days): "))
        max_rent_period = int(input("Enter maximum rent period (in days): "))
        return make, model, year, mileage, available_now, min_rent_period, max_rent_period

    def get_user_preferences(self):
        """Prompt the user for their car preferences."""
        print("Enter your car preferences:")
        make = input("Preferred make: ")
        model = input("Preferred model: ")
        min_price = input("Minimum price: ")
        max_price = input("Maximum price: ")
        min_year = input("Minimum year: ")
        max_year = input("Maximum year: ")

        return {
            'make': make,
            'model': model,
            'min_price': min_price,
            'max_price': max_price,
            'min_year': min_year,
            'max_year': max_year
        }

    def display_cars(self, cars):
        """Display a list of available cars."""
        if not cars:
            print("No cars available.")
            return
        for car in cars:
            print(f"ID: {car['id']}, Make: {car['make']}, Model: {car['model']}, Year: {car['year']}, "
                  f"Mileage: {car['mileage']}, Available: {car['available_now']}, "
                  f"Min Rent Period: {car['min_rent_period']} days, Max Rent Period: {car['max_rent_period']} days")

    def confirm_deletion(self):
        """Ask for confirmation before deleting a car."""
        confirmation = input("Are you sure you want to delete this car? (yes/no): ")
        return confirmation.lower() == 'yes'

    def show_add_success(self):
        """Display a success message for adding a car."""
        print("Car added successfully.")

    def show_update_success(self):
        """Display a success message for updating a car."""
        print("Car updated successfully.")

    def show_deletion_success(self):
        """Display a success message for deleting a car."""
        print("Car deleted successfully.")
