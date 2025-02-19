#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 5, 2025

# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).


year = int(input("Greetings! What is your year of origin? "))

# Fixed condition (before 1900)
if year < 1900:  
    print("Woah, that's the past!")
    
# Corrected logical condition   
elif 1900 <= year < 2020:  
    print("That's totally the present!")
    
# Changed `elif:` to `else`   
else:  
    print("Far out, that's the future!!")
