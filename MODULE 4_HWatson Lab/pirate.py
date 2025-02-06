#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 6, 2025

# This program prompts the user for a password and checks if they are a pirate. 
# If the user enters "Arrr!", they are identified as a pirate and asked to go away.
# Otherwise, they are greeted as a "hater of pirates."

# Ask the user for a password input
greeting = input("Hello, possible pirate! What's the password? ")  # Fixed missing closing quote

# Check if the input matches the pirate password
if greeting in ["Arrr!"]:  # Fixed incorrect closing bracket placement
    print("Go away, pirate.")
else:  # Fixed incorrect `elif` usage (no condition)
    print("Greetings, hater of pirates!")  # Fixed indentation

