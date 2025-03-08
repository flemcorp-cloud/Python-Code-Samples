#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: March 8, 2025

# A program that takes a year as a parameter and returns True
# if the year is a leap year, False if it is otherwise.
# It will tell the user if the year input is leap year or not.

def is_leap_year(year):
    # Check if year is divisible by 4
    if year % 4 == 0:
        # If year is divisible by 100, check if it's also divisible by 400
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Divisible by 400 — it's a leap year
            else:
                return False  # Divisible by 100 but not 400 — not a leap year
        else:
            return True  # Divisible by 4 but not 100 — it's a leap year
    else:
        return False  # Not divisible by 4 — not a leap year

# Prompt the user to enter a year and check if it is a leap year using the is_leap_year() function
year = int(input("Enter a year to check if it's a leap year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


