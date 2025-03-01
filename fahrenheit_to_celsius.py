#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: January 30, 2025
# This program converts Fahrenheit to Celsius temperature

while True:
    try:
        # Prompt the user to enter temperature in Fahrenheit
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        
        # Convert Fahrenheit to Celsius
        celsius = (fahrenheit - 32) * 5 / 9
        
        # Print the result with a friendly message
        print(f"{fahrenheit}° Fahrenheit is equal to {celsius:.2f}° Celsius.")
        break  # Exit loop after successful input
        
    except ValueError:
        print("Invalid input. Please enter a numeric value for the temperature.")
