#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 27, 2025

# Problem 3: A program that will multiply all the numbers in a list.
# Use list [5, 2, 7, -1].



def multiply_list(numbers):
    """Multiplies all the numbers in a given list."""
    result = 1  # Start with 1 because multiplying by 0 results in 0
    for num in numbers:  # Loop through each number in the list
        result *= num  # Multiply each number with the result
    return result  # Return the final product

# Given list
num_list = [5, 2, 7, -1]

# Call the function and print the result
product = multiply_list(num_list)
print(f"The product of {num_list} is: {product}")
