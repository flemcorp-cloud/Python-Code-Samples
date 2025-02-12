#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 12, 2025

# a program that iterates the integers from 1 to 50 and checks if the numbers
# are divisible by 3, 5 or both

# Iterate from 1 to 50
for i in range(1, 51):
    # Check if the number is divisible by both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        print("Divisible by both")
    # Check if the number is divisible by 3
    elif i % 3 == 0:
        print("Divisible by three")
    # Check if the number is divisible by 5
    elif i % 5 == 0:
        print("Divisible by five")
    # If the number is not divisible by 3 or 5, print the number itself
    else:
        print(i)
