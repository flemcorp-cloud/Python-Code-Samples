#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 27, 2025

# Problem 4: A program that takes a list of numbers and returns a new list with
# unique elements of the first list. Use list [1, 3, 3, 3, 6, 2, 3, 5].
# It also uses the append function.

def unique_elements(numbers):
    """Returns a new list with unique elements from the given list."""
    unique_list = []  # Initialize an empty list to store unique elements

    for num in numbers:  # Loop through each number in the input list
        if num not in unique_list:  # Check if the number is already in unique_list
            unique_list.append(num)  # Append only if it's not already in the list
    
    return unique_list  # Return the new list with unique elements

# Given list
num_list = [1, 3, 3, 3, 6, 2, 3, 5]

# Call the function and print the result
unique_numbers = unique_elements(num_list)
print(f"Unique elements from {num_list} are: {unique_numbers}")
