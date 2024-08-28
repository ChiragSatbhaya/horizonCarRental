
---

# Horizon Car Rental System

## Overview

The Horizon Car Rental System is designed to automate the car rental process, improving efficiency and enhancing customer satisfaction. This system allows users to register, log in, view available cars, and book rentals, while providing admins with tools to manage cars and rental bookings.

## Table of Contents

- [Installation](#installation)
- [File Descriptions](#file-descriptions)
- [Usage](#usage)
- [Licensing](#licensing)
- [Known Issues](#known-issues)
- [Credits](#credits)

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/horizon-car-rental.git
   cd horizon-car-rental
   ```

2. **Install Dependencies**
   Ensure you have Python 3.8+ installed. Install required packages using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the Database**
   Edit the database configuration file `config/db_config.py` to include your database connection details.

4. **Run Migrations**
   If applicable, run database migrations to set up the required schema:
   ```bash
   python manage.py migrate
   ```

5. **Start the Application**
   ```bash
   python main.py
   ```

## File Descriptions

- **`config/`**:
  - **`db_config.py`**: Contains database configuration settings.

- **`models/`**:
  - **`car.py`**: Defines the `Car` class for managing car-related operations.
  - **`crud_operations.py`**: Provides CRUD operations and database interactions.
  - **`db_connection.py`**: Manages database connection and query execution.
  - **`rental.py`**: Handles rental operations such as creating, approving, and rejecting rentals.
  - **`user.py`**: Manages user authentication, registration, and role differentiation.

- **`controllers/`**:
  - **`admin_controller.py`**: Handles admin-specific functionalities for car and rental management.
  - **`car_controller.py`**: Manages car-related operations from the user perspective.
  - **`rental_controller.py`**: Manages rental bookings and related operations.
  - **`user_controller.py`**: Manages user registration, login, and profile management.

- **`views/`**:
  - **`admin_view.py`**: Provides admin views for managing users and cars.
  - **`car_view.py`**: Facilitates car management and display of car information.
  - **`rental_view.py`**: Handles rental-related interactions and displays.
  - **`user_view.py`**: Manages user interactions for registration and login.

- **`main.py`**: Entry point for the application, initializes and runs the system.

## Usage

1. **User Registration and Login**
   - Register a new account or log in using the provided user interface.

2. **Car Management**
   - Admins can add, update, or delete car records through the admin view interface.

3. **Car Booking**
   - Customers can view available cars, select a car, and book rentals specifying dates and details.

4. **Rental Management**
   - Admins can approve or reject rental requests.

## Licensing

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Known Issues

- **Bug**: The rental fee calculation may not handle discounts correctly. A fix is in progress.
- **Feature Request**: A mobile-friendly interface is planned for future releases.

## Credits

Developed by [Chirag Satbhaya](https://github.com/ChiragSatbhaya). Special thanks to contributors and open-source libraries used in this project.

---