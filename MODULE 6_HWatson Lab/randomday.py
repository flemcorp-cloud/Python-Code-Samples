#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 19, 2025

# Problem 3: A program that will select and print a random day of the week.

import random

# Function to select and print a random day of the week
def select_random_day():
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    selected_day = random.choice(days_of_week)  # Randomly selects a day from the list
    print(f"The randomly selected day of the week is: {selected_day}")

# Main function to execute the random day selection
def main():
    select_random_day()

# Check if the script is being run directly
if __name__ == "__main__":
    main()
