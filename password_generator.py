import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))


def main():
    print("=== Password Generator ===")

    try:
        length = int(input("Enter password length: "))

        if length < 4:
            print("Password length must be at least 4.")
            return

        password = generate_password(length)
        print(f"Generated password: {password}")

    except ValueError:
        print("Please enter a valid number.")


if name == "main":
    main()