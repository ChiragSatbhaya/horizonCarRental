# Test script to verify read_user functionality
from models.crud_operations import CrudOperations
import mysql.connector

from models.db_connection import Database

db_connection_instance = Database()

# Pass the db_connection_instance to CrudOperations
crud = CrudOperations(db_connection_instance)

username = 'horizonadmin'  # Replace with your test username
user = crud.read_user(username)

if user:
    print(f"User found: {user}")
else:
    print("User not found.")
