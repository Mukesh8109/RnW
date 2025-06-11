import math


def calculate_fact():
    print("\n--- Factorial --- \n")
    number = int(input("Enter a number:"))
    fact = 1
    for i in range(1,number+1):
        fact *= i#factorial calculate if number 5 loop flip up to 1 to 5

    print(f"Factorial:{fact}")
    print("="*60)


def calculate_compoundrate():
    print("\n--- Compound Interest Calculator ---\n")

    p = float(input("Enter principal amount: "))
    r = float(input("Enter annual interest rate (in %): "))
    n = int(input("Enter time (in years): "))

    # Compound Interest formula
    amount = p * (1 + r / 100) ** n
    compound_interest = amount - p

    print(f"Compound Interest: {compound_interest:.2f}")
    print(f"Total Amount after {n} years: {amount:.2f}")
    print("="*60)


def trigonometric_calculation():
    print("\n-- Trigonometric Calculator ---\n")

    angle_deg = float(input("Enter the angle(in degree):"))

    angle_rad = math.radians(angle_deg)

    sin = math.sin(angle_rad)
    cos = math.cos(angle_rad)
    tan = math.tan(angle_rad)

    print(f"Sin({angle_deg}) = {sin:.2f}")
    print(f"Cos({angle_deg}) = {cos:.2f}")
    print(f"Tan({angle_deg}) = {tan:.2f}")
    print("="*60)


def geometric_shape_calculator():
    print("\n--- Geometric Shape Calculator ---\n")#provide the menu for shape
    print("Choose a shape:")
    print("1. Square")
    print("2. Rectangle")
    print("3. Circle")
    print("4. Triangle")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        side = float(input("Enter the side length of the square: "))
        area = side * side#area calculate
        perimeter = 4 * side#perimeter calculate
        print(f"Area: {area:.2f}, Perimeter: {perimeter:.2f}")

    elif choice == '2':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width#area calculate
        perimeter = 2 * (length + width)#perimeter calculate
        print(f"Area: {area:.2f}, Perimeter: {perimeter:.2f}")

    elif choice == '3':
        radius = float(input("Enter the radius of the circle: "))
        area = math.pi * radius ** 2#area calculat
        perimeter = 2 * math.pi * radius#perimeter calculate
        print(f"Area: {area:.2f}, Circumference: {perimeter:.2f}")

    elif choice == '4':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        side1 = float(input("Enter the length of side 1: "))
        side2 = float(input("Enter the length of side 2: "))
        area = 0.5 * base * height#area calculat
        perimeter = base + side1 + side2#perimeter calculate
        print(f"Area: {area:.2f}, Perimeter: {perimeter:.2f}")

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")




