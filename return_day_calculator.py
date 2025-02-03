#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: January 30, 2025
# Program will calculate the return day based on starting day & length of stay

while True:
    try:
        # Prompt the user to enter the starting day number (0-6)
        start_day = int(input("Enter the starting day number (0-6) where 0 is Sunday: "))
        
        # Check if the input is valid (0-6)
        if start_day < 0 or start_day > 6:
            print("Invalid input. Please enter a day number between 0 and 6.")
            continue
        
        # Prompt the user to enter the length of the stay in nights
        stay_length = int(input("Enter the number of nights of your stay: "))
        
        # Check if the stay length is a positive number
        if stay_length < 0:
            print("Stay length must be a non-negative number. Please try again.")
            continue
        
        # Calculate the return day (starting day + length of stay)
        return_day = (start_day + stay_length) % 7  # Use modulo 7 to wrap around the week
        
        # Print the result
        print(f"You will return on day number {return_day} of the week.")
        break  # Exit loop after successful input
        
    except ValueError:
        print("Invalid input. Please enter numeric values.")
