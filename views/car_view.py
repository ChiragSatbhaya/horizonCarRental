class CarView:
    def get_car_details(self):
        """Prompt for car details to add or update a car."""
        make = input("Enter car make: ").strip()
        model = input("Enter car model: ").strip()

        while True:
            try:
                year = int(input("Enter car year (e.g., 2022): "))
                mileage = int(input("Enter car mileage: "))
                min_rent_period = int(input("Enter minimum rent period (in days): "))
                max_rent_period = int(input("Enter maximum rent period (in days): "))
                if min_rent_period > 0 and max_rent_period >= min_rent_period:
                    break
                else:
                    print("Min rent period must be > 0 and max rent period must be >= min rent period.")
            except ValueError:
                print("Invalid input. Please enter valid integers for year, mileage, and rent periods.")

        available_now = input("Is the car available now? (yes/no): ").strip().lower() == 'yes'
        return make, model, year, mileage, available_now, min_rent_period, max_rent_period

    def get_user_preferences(self):
        """Prompt the user for their car preferences."""
        make = input("Preferred make: ").strip()
        model = input("Preferred model: ").strip()

        while True:
            try:
                min_price = float(input("Minimum price: "))
                max_price = float(input("Maximum price: "))
                min_year = int(input("Minimum year: "))
                max_year = int(input("Maximum year: "))
                if min_price >= 0 and max_price >= min_price and min_year > 0 and max_year >= min_year:
                    break
                else:
                    print("Invalid range. Ensure prices and years are valid.")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

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