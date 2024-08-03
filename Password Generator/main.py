import secrets
import string

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def generate_passwords(num_passwords, password_length):
    alphabet = string.ascii_letters
    punctuation = string.punctuation
    digits = string.digits
    passwords = []

    for _ in range(num_passwords):
        password = ''.join(secrets.choice(alphabet + punctuation + digits) for _ in range(password_length))
        passwords.append(password)

    return passwords

num_passwords = get_positive_integer("How many passwords you want to generate: ")
password_length = get_positive_integer("Enter the length of the passwords: ")

passwords = generate_passwords(num_passwords, password_length)

for password in passwords:
    print(password)