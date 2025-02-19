#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 19, 2025

# Problem 6: Program that uses a For statement to calculate the factorial of a user input value.
# It will print this value as well as the calculated value using the factorial function in the math module.

import math

# Function to calculate factorial using a for loop
def factorial_for_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i  # Multiply result by each number in the range
    return result

# Main function
def main():
    # Get user input
    n = int(input("Enter a positive integer: "))
    
    # Calculate factorial using custom function
    calculated_factorial = factorial_for_loop(n)
    print(f"Factorial of {n} using for loop: {calculated_factorial}")
    
    # Calculate factorial using math.factorial()
    math_factorial = math.factorial(n)
    print(f"Factorial of {n} using math.factorial: {math_factorial}")

# Check if the script is being run directly
if __name__ == "__main__":
    main()
