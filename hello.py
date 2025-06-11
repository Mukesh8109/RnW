import datetime
import math
import random
import string
import uuid

# ==== Utility Functions ====
def get_current_datetime():
    return datetime.datetime.now()

def compute_factorial(n):
    try:
        return math.factorial(n)
    except ValueError:
        return "Invalid input. Please enter a non-negative integer."

def calculate_area_of_circle(radius):
    return math.pi * radius ** 2

def generate_random_number(start, end):
    return random.randint(start, end)

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_uuid():
    return str(uuid.uuid4())

# ==== Menu ====
def show_menu():
    print("\n=== Multi-Utility Toolkit Menu ===")
    print("1. Show current date and time")
    print("2. Compute factorial")
    print("3. Calculate area of a circle")
    print("4. Generate random number")
    print("5. Generate random string")
    print("6. Generate UUID")
    print("7. Exit")

# ==== Main Program ====
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1–7): ").strip()

        match choice:
            case '1':
                print(f"Current Date and Time: {get_current_datetime()}")
            case '2':
                n = int(input("Enter a non-negative integer: "))
                print(f"Factorial of {n}: {compute_factorial(n)}")
            case '3':
                r = float(input("Enter radius of the circle: "))
                print(f"Area of circle: {calculate_area_of_circle(r):.2f}")
            case '4':
                start = int(input("Enter start of range: "))
                end = int(input("Enter end of range: "))
                print(f"Random Number: {generate_random_number(start, end)}")
            case '5':
                length = int(input("Enter length of random string: "))
                print(f"Random String: {generate_random_string(length)}")
            case '6':
                print(f"Generated UUID: {generate_uuid()}")
            case '7':
                print("Exiting... Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
