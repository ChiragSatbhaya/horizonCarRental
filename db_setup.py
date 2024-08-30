import mysql.connector
from mysql.connector import Error
import config

def create_database():
    try:
        # Connect to MySQL
        connection = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD
        )
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {config.DB_NAME}")
        print(f"Database '{config.DB_NAME}' created or already exists.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def create_tables():
    try:
        connection = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME
        )
        cursor = connection.cursor()

        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(100) NOT NULL,
                password VARCHAR(255) NOT NULL,
                role ENUM('admin', 'user') NOT NULL DEFAULT 'user'
            ) DEFAULT CHARSET=utf8;
        """)

        # Create cars table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cars (
                id INT AUTO_INCREMENT PRIMARY KEY,
                make VARCHAR(100) NOT NULL,
                model VARCHAR(100) NOT NULL,
                year INT NOT NULL,
                mileage INT NOT NULL,
                available_now BOOLEAN NOT NULL DEFAULT TRUE,
                min_rent_period INT NOT NULL,
                max_rent_period INT NOT NULL,
                daily_rate DECIMAL(10, 2) NULL
            )
        """)

        # Create rentals table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS rentals (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                car_id INT NOT NULL,
                start_date DATE NOT NULL,
                end_date DATE NOT NULL,
                total_cost DECIMAL(10, 2) NOT NULL,
                status ENUM('Pending', 'Approved', 'Rejected') NOT NULL DEFAULT 'Pending',
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (car_id) REFERENCES cars(id)
            )
        """)

        print("Tables created successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
    create_tables()