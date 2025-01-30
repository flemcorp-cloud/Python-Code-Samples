#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: January 30, 2025
# Program to calculate the Miles Per Gallon (MPG) for a car

while True:
    try:
        # Prompt the user to enter miles driven and gallons used
        miles = float(input("Enter the number of miles driven: "))
        gallons = float(input("Enter the number of gallons used: "))
        
        # Check for valid input (gallons cannot be zero)
        if gallons <= 0:
            print("Gallons used must be greater than zero. Please try again.")
            continue
        
        # Calculate the MPG
        mpg = miles / gallons
        
        # Print the result with a friendly message
        print(f"The car's MPG is {mpg:.2f} miles per gallon.")
        break  # Exit loop after successful input
        
    except ValueError:
        print("Invalid input. Please enter numeric values for both miles and gallons.")
