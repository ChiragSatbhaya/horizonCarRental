from controllers.admin_controller import AdminController
from controllers.user_controller import UserController
from controllers.car_controller import CarController
from controllers.rental_controller import RentalController
from models.db_connection import Database
from models.car import Car

def main():
    # Initialize the database connection
    db = Database()

    # Pass the database connection to the controllers
    admin_controller = AdminController(db)
    user_controller = UserController(db)
    car_controller = CarController(db)
    rental_controller = RentalController(db)

    while True:
        print("\nWelcome to Horizon Car Rental System")
        print("1. Admin Login")
        print("2. User Registration")
        print("3. User Login")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            admin = admin_controller.login()
            if admin:
                admin_menu(admin_controller, car_controller, rental_controller)
        elif choice == '2':
            user_controller.register()
        elif choice == '3':
            user = user_controller.login()
            if user:
                user_menu(user, car_controller, rental_controller)
        elif choice == '4':
            print("Thank you for using Horizon Car Rental System. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def admin_menu(admin_controller, car_controller, rental_controller):
    while True:
        print("\nAdmin Menu")
        print("1. Manage Cars")
        print("2. Manage Rentals")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            manage_cars(car_controller)
        elif choice == '2':
            manage_rentals(rental_controller)
        elif choice == '3':
            print("Logging out...")
            break
        else:
            print("Invalid choice, please try again.")

def user_menu(user, car_controller, rental_controller):
    while True:
        print(f"\nUser Menu - Welcome {user.get('username', 'User')}")
        print("1. View Available Cars")
        print("2. Make a Booking")
        print("3. View Your Bookings")
        print("4. Get Car Recommendations")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            car_controller.view_available_cars()
        elif choice == '2':
            rental_controller.book_car(user)
        elif choice == '3':
            print(f"User details: {user}")  # Debug statement
            rental_controller.view_user_bookings(user)
        elif choice == '4':
            car_controller.recommend_cars(user)
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice, please try again.")

def manage_cars(car_controller):
    while True:
        print("\nCar Management")
        print("1. Add Car")
        print("2. Update Car")
        print("3. Delete Car")
        print("4. View All Cars")
        print("5. Back to Admin Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            car_controller.add_car()
        elif choice == '2':
            car_id = int(input("Enter the ID of the car to update: "))
            car_controller.update_car(car_id)
        elif choice == '3':
            car_id = int(input("Enter the ID of the car to delete: "))
            car_controller.delete_car(car_id)
        elif choice == '4':
            car_controller.view_all_cars()
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

def manage_rentals(rental_controller):
    while True:
        print("\nRental Management")
        print("1. View All Rentals")
        print("2. Approve/Reject Rental")
        print("3. Back to Admin Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            rental_controller.view_all_rentals()
        elif choice == '2':
            rental_controller.manage_rentals()
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
