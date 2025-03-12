#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: March 11, 2025

# A program that uses a while loop, creates a list called L that contains the numbers 0 to 10. On each
# iteration, the loop appends the current value of a counter variable to the list and then
# increases the counter by 1. The while loop will stop once the counter variable is greater than 10. 

# Initialize an empty list
L = []

# Initialize the counter variable
counter = 0

# Run the loop while the counter is less than or equal to 10
while counter <= 10:
    L.append(counter)  # Append the current counter value to the list
    counter += 1  # Increase the counter by 1

# Print the final list
print("List L:", L)
