#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: March 8, 2025

# A program that allows the user to input 2 numbers for comparison
# and and prints whether they are equal or not.

def compare_numbers():
    # Ask the user for the first number and convert it to a float
    num1 = float(input("Enter the first number: "))

    # Ask the user for the second number and convert it to a float
    num2 = float(input("Enter the second number: "))

    # Compare the two numbers
    if num1 == num2:
        # If the numbers are equal, print this message
        print("The two numbers are equal.")
    else:
        # If the numbers are not equal, print this message
        print("The two numbers are not equal.")

# Call the function to actually run the comparison when the script is executed
compare_numbers()
