from models.crud_operations import CrudOperations

class Car:
    def __init__(self, db):
        self.db = db
        self.crud = CrudOperations(db)

    def add_car(self, make, model, year, mileage, available_now, min_rent_period, max_rent_period):
        """Add a new car to the database."""
        query = """
            INSERT INTO cars (make, model, year, mileage, available_now, min_rent_period, max_rent_period) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        self.crud.db.execute_query(query, (make, model, year, mileage, available_now, min_rent_period, max_rent_period))

    def update_car(self, car_id, make, model, year, mileage, available_now, min_rent_period, max_rent_period):
        """Update the details of an existing car."""
        query = """
            UPDATE cars 
            SET make=%s, model=%s, year=%s, mileage=%s, available_now=%s, min_rent_period=%s, max_rent_period=%s 
            WHERE id=%s
        """
        self.crud.db.execute_query(query, (make, model, year, mileage, available_now, min_rent_period, max_rent_period, car_id))

    def delete_car(self, car_id):
        """Delete a car from the database."""
        query = "DELETE FROM cars WHERE id=%s"
        self.crud.db.execute_query(query, (car_id,))

    def get_available_cars(self):
        """Retrieve all cars that are currently available."""
        query = "SELECT * FROM cars WHERE available_now=1"
        cars = self.crud.db.fetchall(query, dictionary=True)
        return cars

    def get_car_by_id(self, car_id):
        """Retrieve a car's details by its ID."""
        query = "SELECT * FROM cars WHERE id = %s"
        result = self.crud.fetchone(query, (car_id,))
        if result:
            return result
        else:
            print(f"No car found with ID {car_id}.")
            return None

    def get_all_cars(self):
        """Retrieve all cars from the database, regardless of availability."""
        query = "SELECT * FROM cars"
        cars = self.crud.db.fetchall(query)
        for car in cars:
            print(f"ID: {car[0]}, Make: {car[1]}, Model: {car[2]}, Year: {car[3]}, Mileage: {car[4]}, "
                  f"Available Now: {car[5]}, Min Rent Period: {car[6]}, Max Rent Period: {car[7]}")
        return self.crud.db.fetchall(query, dictionary=True)

    def update_car_availability(self, car_id, available):
        """Update the availability of a car."""
        query = "UPDATE cars SET available_now = %s WHERE id = %s"
        try:
            self.db.execute_query(query, (available, car_id))
            print(f"Car {car_id} availability updated successfully.")
        except Exception as e:
            print(f"Error updating car availability: {e}")

    def find_cars_by_preferences(self, preferences):
        """Find cars based on user preferences."""
        query = """
            SELECT * FROM cars WHERE available_now = 1
            AND make LIKE %s
            AND model LIKE %s
            AND daily_rate BETWEEN %s AND %s
            AND year BETWEEN %s AND %s
        """
        params = (
            f"%{preferences['make']}%",
            f"%{preferences['model']}%",
            preferences['min_price'],
            preferences['max_price'],
            preferences['min_year'],
            preferences['max_year']
        )
        try:
            return self.db.fetchall(query, params, dictionary=True)
        except Exception as e:
            print(f"Error fetching cars by preferences: {e}")
            return []