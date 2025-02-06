#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: January 29, 2025
# This program calculates the area of a circle based on user input.

import math  # Import math module for π (pi)

while True:
    try:
        # Prompt the user to enter the radius
        radius = float(input("Enter the radius of the circle: "))
        
        # Ensure the radius is non-negative
        if radius < 0:
            print("Radius cannot be negative. Please enter a valid number.")
            continue
        
        # Compute the area
        area = math.pi * radius ** 2
        
        # Print the result with a friendly message
        print(f"The area of the circle with radius {radius} is {area:.2f} square units.")
        break  # Exit loop after successful input
        
    except ValueError:
        print("Invalid input. Please enter a numeric value for the radius.")
