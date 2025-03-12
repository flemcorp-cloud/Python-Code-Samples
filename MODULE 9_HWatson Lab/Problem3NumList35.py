#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: March 11, 2025

# A program that uses a while loop & asks the user to enter a number. Appends each entered number
# to a list and adds them together. Continues asking for a number until the sum of the list of
# numbers is greater than 100

# Initialize an empty list to store the numbers
numbers = []

# Initialize the sum to 0
total = 0

# Keep asking for a number until the sum exceeds 100
while total <= 100:
    try:
        num = float(input("Enter a number: "))  # Get user input and convert to float
        numbers.append(num)  # Append the number to the list
        total += num  # Update the sum
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Display the results
print("\nFinal List of Numbers:", numbers)
print("Total Sum:", total)
