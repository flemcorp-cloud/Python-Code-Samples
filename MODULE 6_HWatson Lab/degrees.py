#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 19, 2025

# Problem 5: A program that will convert radians to degrees given a user input value. 
# This value as well as the calculated value using the degrees function in the math module will be printed.

import math

# Function to convert radians to degrees
def radians_to_degrees(radians):
    degrees = radians * (180 / math.pi)  # Conversion formula
    return degrees

# Main function
def main():
    # Get user input for radians
    radians = float(input("Enter a value in radians: "))
    
    # Convert using the custom function
    converted_degrees = radians_to_degrees(radians)
    print(f"Converted value from radians to degrees: {converted_degrees}°")
    
    # Convert using the math.degrees() function
    math_degrees = math.degrees(radians)
    print(f"Value using math.degrees: {math_degrees}°")

# Check if the script is being run directly
if __name__ == "__main__":
    main()
