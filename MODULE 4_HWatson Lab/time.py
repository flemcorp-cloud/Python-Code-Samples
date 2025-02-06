#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 6, 2025


# This program calculates the time on a 24-hour clock after waiting a specified number of hours.

# Get the current time from the user (0-23 hours)
currentTimeStr = input("What is the current time (in hours 0-23)? ")

# Get the wait time from the user
waitTimeStr = input("How many hours do you want to wait? ")  # Fixed missing closing parenthesis

# Convert input strings to integers
currentTimeInt = int(currentTimeStr)  # Fixed incorrect variable name
waitTimeInt = int(waitTimeStr)  # Fixed incorrect variable name

# Calculate the final time on a 24-hour clock
finalTimeInt = (currentTimeInt + waitTimeInt) % 24  # Use modulo to keep within 24-hour format

# Print the final time
print("The time after waiting will be:", finalTimeInt)  # Fixed incorrect variable name
