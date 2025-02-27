#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 27, 2025

# Problem 1: A program that returns the area of a circle of radius r depending on the number input.

import math  # Importing the math module to use the constant pi

def areaOfCircle(r):
    """Returns the area of a circle with radius r."""
    return math.pi * r ** 2  # Formula for the area of a circle: π * r^2

# Ask the user to input the radius
radius = float(input("Enter the radius of the circle: "))  # Convert input to float

# Call the function and store the result in the 'area' variable
area = areaOfCircle(radius)

# Print the result with two decimal places
print(f"The area of a circle with radius {radius} is: {area:.2f}")

