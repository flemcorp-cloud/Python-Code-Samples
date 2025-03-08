#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: March 8, 2025

# A program that takes two inputs from a user and prints whether
# the sum is greater than 10, less than 10, or equal to 10.

def check_sum():
    # Ask the user for two numbers and convert them to floats
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculate the sum of the two numbers
    total = num1 + num2

    # Check whether the sum is greater than, less than, or equal to 10
    if total > 10:
        print("The sum is greater than 10.")
    elif total < 10:
        print("The sum is less than 10.")
    else:
        print("The sum is exactly 10.")

# Call the function to run it
check_sum()
