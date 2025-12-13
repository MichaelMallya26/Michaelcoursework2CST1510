from operator import truediv

import bcrypt
import os
def hash_password(plain_text_password):
    # TODO: Encode the password to bytes (bcrypt requires byte strings)
    password_bytes = plain_text_password.encode("utf-8")
    # TODO: Generate a salt using bcrypt.gensalt()
    salt = bcrypt.gensalt()
    # TODO: Hash the password using bcrypt.hashpw()
    hashed = bcrypt.hashpw(password_bytes, salt)
    # TODO: Decode the hash back to a string to store in a text file
    return hashed.decode("utf-8")

def verify_password():
    # TODO: Encode both the plaintext password and the stored hash to byte
    # TODO: Use bcrypt.checkpw() to verify the password
    # This function extacts the salt from the hash and compares
    return

# TEMPOROARY TEST CODE - Remove after testing
test_password = "SecurePassword123"

# Test hashing
hashed = hash_password(test_password)
print(f"Original Password: {test_password}")
print(f"Hashed Password: {hashed}")
print(f"Hash length: {len(hashed)} characters")

def verify_password(password: str, hashed: str)-> bool:


#Test verification with correct password
is_valid = verify_password(test_password, hashed)
print(f"\nVerification with correct password: {is_valid}")


# Test verification with incorrect password
is_valid = verify_password("wrong password", hashed)
print(f"\nVerification with incorrect password: {is_valid}")

USER_DATA_FILE= "users.txt"

def register_user(username, password):
    #TODO: Check if the username already exists
    #TODO: Hash the password
    #TODO: Append the new user to the file
    #format: username, hashed_password
    return True

def user_exists(username):

    def login_user(username, password):
        return True
# TODO: Handle the case where no users are registered yet
# TODO: Search for the username in the file
# TODO: If username matches, verify the password
# TODO: If we reach here, the username was not found

def validate_user(username):
    pass
def validate_password(password):
    pass
def display_menu():
    """Displays the main menu options."""
    print("\n" + "=" * 50)
    print("  MULTI-DOMAIN INTELLIGENCE PLATFORM")
    print("  Secure Authentication System")
    print("=" * 50)
    print("\n[1] Register a new user")
    print("[2] Login")
    print("[3] Exit")
    print("-" * 50)


def main():
    """Main program loop."""
    print("\nWelcome to the Week 7 Authentication System!")

    while True:
        display_menu()
        choice = input("\nPlease select an option (1-3): ").strip()

        if choice == '1':
            # Registration flow
            print("\n--- USER REGISTRATION ---")
            username = input("Username: ")

