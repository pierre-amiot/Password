import json
import random
import string
import hashlib

PASSWORD_FILE = "passwords.json"

def load_passwords():
    try:
        with open(PASSWORD_FILE, "r") as f:
            passwords = json.load(f)
    except FileNotFoundError:
        passwords = {}
    return passwords

def save_passwords(passwords):
    with open(PASSWORD_FILE, "w") as f:
        json.dump(passwords, f)

def password_is_valid(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in '!@#$%^&*' for char in password):
        return False
    return True

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + '!@#$%^&*'
    password = ''.join(random.choice(alphabet) for i in range(length))
    return password

def add_password(passwords):
    while True:
        username = input("Entrez un nom d'utilisateur : ")
        if username in passwords:
            print("Ce nom d'utilisateur est déjà utilisé.")
        else:
            break

    while True:
        password = input("Entrez un mot de passe : ")
        if password_is_valid(password):
            break
        else:
            print("Le mot de passe doit contenir au moins 8 caractères, une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial (!, @, #, $, %, ^, &, *)")

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    passwords[username] = hashed_password
    save_passwords(passwords)
    print("Le mot de passe a été ajouté avec succès !")

def show_passwords(passwords):
    for username, hashed_password in passwords.items():
        print(f"{username}: {hashed_password}")

def main():
    passwords = load_passwords()

    while True:
        print("Que souhaitez-vous faire ?")
        print("1. Ajouter un mot de passe")
        print("2. Afficher les mots de passe")
        print("3. Quitter")
        choice = input("Entrez le numéro de votre choix : ")

        if choice == "1":
            add_password(passwords)
        elif choice == "2":
            show_passwords(passwords)
        elif choice == "3":
            break
        else:
            print("Choix invalide.")

    print("Merci d'avoir utilisé notre programme !")

if __name__ == "__main__":
    main()