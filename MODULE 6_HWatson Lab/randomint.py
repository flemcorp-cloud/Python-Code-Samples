#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 19, 2025

# Problem 2: Program that generates & prints a random odd integer between 0 & 100 

import random

# Function to generate and print a random odd integer between 0 and 100
def generate_odd_integer():
    odd_integer = random.randrange(1, 101, 2)  # Start at 1, go up to 101, step by 2 (odd numbers)
    print(f"Random odd integer between 0 and 100: {odd_integer}")

# Main function to execute the random odd integer generation
def main():
    generate_odd_integer()

# Check if the script is being run directly
if __name__ == "__main__":
    main()
