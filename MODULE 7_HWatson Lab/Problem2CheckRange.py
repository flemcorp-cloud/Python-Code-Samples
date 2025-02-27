#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 27, 2025

# Problem 2: A program that checks whether a number is in a given range. Uses
# range(1,10). Prints whether the number is in or not in the range.



def check_number_in_range(num):
    """Checks if a number is in the range 1 to 9 (inclusive)."""
    
    # Check if the number is within the range 1 to 9
    if num in range(1, 10):  
        print(f"{num} is in the range (1 to 9).")
    else:
        print(f"{num} is NOT in the range (1 to 9).")

# Loop until the user enters a valid number
while True:
    try:
        # Get user input and attempt to convert it to an integer
        number = int(input("Enter a number: "))
        
        # Call the function with the valid integer input
        check_number_in_range(number)
        break  # Exit the loop if input is valid

    except ValueError:
        # Handle non-integer inputs
        print("Invalid input! Please enter a valid integer.")
