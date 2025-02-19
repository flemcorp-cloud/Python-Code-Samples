#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 19, 2025

# Problem 1: A program that will print 10 random integers between 25 and 35.


import random

# Function to generate and print 10 random integers between 25 and 35.
def generate_random_numbers():
    for _ in range(10):
        print(random.randrange(25, 36))  # Generates random number between 25 and 35

def main():
# Main function to execute the random number generation.
    print("10 Random integers between 25 and 35:")
    generate_random_numbers()

if __name__ == "__main__":
    main()
