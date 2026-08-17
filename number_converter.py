def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def kilometers_to_miles(kilometers):
    return kilometers * 0.621371


def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462


def main():
    print("=== Number Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Kilometers to Miles")
    print("3. Kilograms to Pounds")

    choice = input("Choose an option: ")

    try:
        value = float(input("Enter value: "))

        if choice == "1":
            result = celsius_to_fahrenheit(value)
            print(f"{value}°C = {result:.2f}°F")

        elif choice == "2":
            result = kilometers_to_miles(value)
            print(f"{value} km = {result:.2f} miles")

        elif choice == "3":
            result = kilograms_to_pounds(value)
            print(f"{value} kg = {result:.2f} pounds")

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter a valid number.")


if name == "main":
    main()