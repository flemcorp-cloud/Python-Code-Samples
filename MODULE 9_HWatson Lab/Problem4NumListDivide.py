#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: March 11, 2025

# A program that runs a while loop that initializes a counter at 0 and will run until the counter
# reaches 50. If the value of the counter is divisible by 10, append the value to the list called tens.
# Confirms the list results using a print statement.


# Initialize an empty list to store multiples of 10
tens = []

# Initialize the counter variable
counter = 0

# Run the loop while the counter is less than or equal to 50
while counter <= 50:
    if counter % 10 == 0:  # Check if the counter is divisible by 10
        tens.append(counter)  # Append to the list
    counter += 1  # Increase the counter by 1

# Print the final list of numbers divisible by 10
print("Multiples of 10:", tens)
