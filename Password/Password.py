import random
import string
import hashlib

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

while True:
    password = input("Choisissez un mot de passe : ")
    if password_is_valid(password):
        break
    else:
        print("Le mot de passe doit contenir au moins 8 caractères, une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial (!, @, #, $, %, ^, &, *)")

hashed_password = hashlib.sha256(password.encode()).hexdigest()

print("Le mot de passe est valide et a été crypté avec succès !")
print("Mot de passe : ", password)
print("Mot de passe crypté : ", hashed_password)