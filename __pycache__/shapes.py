import math

def square(side):
    try:
        return side * side
    except ValueError:
        print("Enter only numbers!")

def rectangle(length, breadth):
    try:
        return length * breadth
    except ValueError:
        print("Enter only numbers!")

def triangle(length, width):
    try:
        return (1/2) * length * width
    except ValueError:
        print("Enter only numbers!")

def circle(radius):
    try:
        return math.pi * radius ** 2
    except ValueError:
        print("Enter only numbers!")