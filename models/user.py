import hashlib
from models.crud_operations import CrudOperations

class User:
    def __init__(self, db):
        self.db = db
        self.crud = CrudOperations(db)

    def sha256_hash(self, password):
        """Hash a password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def admin_login(self, username, password):
        """Authenticate an admin login."""
        try:
            user = self.crud.read_user(username)
            if user:
                hashed_password = self.sha256_hash(password)
                if user['password'] == hashed_password and user['role'] == 'admin':
                    return user
                else:
                    print("Admin login failed: Invalid credentials.")
            else:
                print("Admin login failed: User not found.")
            return None
        except Exception as e:
            print(f"Error during admin login: {e}")
            return None

    def register(self, username, password, role):
        """Register a new user with the given username, password, and role."""
        query = """
            INSERT INTO users (username, password, role)
            VALUES (%s, %s, %s)
        """
        try:
            hashed_password = self.sha256_hash(password)
            self.db.execute_query(query, (username, hashed_password, role))
        except Exception as e:
            print(f"Error during user registration: {e}")

    def authenticate(self, username, password):
        """Authenticate a user with the given username and password."""
        query = """
               SELECT id, username, password, role FROM users WHERE username=%s
           """
        try:
            result = self.db.fetchone(query, (username,))
            if result:
                stored_id, stored_username, stored_password, stored_role = result
                if self.sha256_hash(password) == stored_password:
                    return {'id': stored_id, 'username': stored_username, 'role': stored_role}
            return None
        except Exception as e:
            print(f"Error during authentication: {e}")
            return None
