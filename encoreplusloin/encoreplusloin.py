import json
import hashlib

def hash_password(password):
    """Hashes a password using SHA-256 algorithm"""
    return hashlib.sha256(password.encode()).hexdigest()

def add_password(password):
    """Adds a hashed password to the passwords file"""
    with open("passwords.json", "r+") as f:
        data = json.load(f)
        hashed_password = hash_password(password)
        if hashed_password in data.values():
            print("Password already exists")
        else:
            data[password] = hashed_password
            f.seek(0)
            json.dump(data, f, indent=4)
            print("Password added")

def display_passwords():
    """Displays all the passwords in the passwords file"""
    with open("passwords.json", "r") as f:
        data = json.load(f)
        for password, hash in data.items():
            print(f"Password: {password} | Hash: {hash}")

# Example usage
add_password("password123")
add_password("password456")
add_password("password123")  # Should print "Password already exists"
display_passwords()