#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: March 8, 2025

# A program takes a list and prints if the value 5 is in that list.

def check_for_five():
    # Ask the user to enter a list of numbers separated by spaces
    user_input = input("Enter a list of numbers separated by spaces: ")

    # Convert the input string into a list of numbers
    number_list = [int(x) for x in user_input.split()]

    # Check if the value 5 is in the list
    if 5 in number_list:
        print("The value 5 is in the list.")
    else:
        print("The value 5 is not in the list.")

# Run the function
check_for_five()

