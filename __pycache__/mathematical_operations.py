
import shapes
import math

def calculate_factorial():
    try:
        fact = int(input("Enter a number: "))
        print(f"The Factorial of {fact} is: {math.factorial(fact)}")
        math.factorial(fact)
    except ValueError:
        print("enter onlu number!!")

def compund_in(principal,rate,time):
    try:
        amount = principal *math.pow((1+rate/(100)),time)
        a  = amount - principal
        return a
    except ValueError:
        print("enter only number!!")

def trigonometric():
    try:
        degree = float(input("Enter angle in degrees: "))
        angle_degree_to_radians = math.radians(degree)

        sin = math.sin(angle_degree_to_radians)
        cos = math.cos(angle_degree_to_radians)
        tan = math.tan(angle_degree_to_radians)
        
        print(f"sin({degree}) = {sin:.4f}")
        print(f"cos({degree}) = {cos:.4f}")
        print(f"tan({degree}) = {tan:.4f}")
    except ValueError:
        print("enter degrees in number between 0 to 360!!")

