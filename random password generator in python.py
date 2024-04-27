import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to Random Password Generator!")
    while True:
        try:
            length = int(input("Enter the length of the password you want: "))
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            password = generate_password(length)
            print("Your random password is:", password)
            break
        except ValueError as ve:
            print("Invalid input:", ve)
            continue

if __name__ == "__main__":
    main()
