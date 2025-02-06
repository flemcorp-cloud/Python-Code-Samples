#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: January 29, 2025
# This program prompts the user for their name and only greets authorized users.

# Define allowed names
allowed_names = {"Hezekiah Watson", "Nathan Braun"}  # Replace "Instructor" with your actual instructor's name

# Prompt the user for their name
userName = input("What is your name? ").strip()

# Check if the user's name is in the allowed list
if userName in allowed_names:
    print(f"Hello, {userName}!")
else:
    print("You are not authorized to be greeted by the system.")
