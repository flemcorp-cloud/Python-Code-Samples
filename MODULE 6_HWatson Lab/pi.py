#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 19, 2025

# Problem 4: A program that will compute the approximation for pi and then
# print that value as well as the value of math.pi from the math module.


import math

# Function to compute an approximation of pi using the Leibniz formula
def approximate_pi(num_terms):
    approximation = 0
    for i in range(num_terms):
        approximation += ((-1) ** i) / (2 * i + 1)  # Leibniz formula for pi
    return approximation * 4  # Multiply by 4 to approximate pi

# Main function to compute and compare pi approximation
def main():
    num_terms = 100000  # Number of terms to compute the approximation
    approximated_pi = approximate_pi(num_terms)
    print(f"Approximated value of pi: {approximated_pi}")
    print(f"Value of math.pi: {math.pi}")

# Check if the script is being run directly
if __name__ == "__main__":
    main()
