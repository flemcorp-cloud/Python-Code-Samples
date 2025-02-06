#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 6, 2025

# This program calculates the time when the alarm will go off after waiting a specified number of hours.

# Get the current time and wait time from the user as strings
str_time = input("What time is it now? ")
str_wait_time = input("What is the number of hours to wait? ")

# Convert the input strings to integers
time = int(str_time)
wait_time = int(str_wait_time)  # Fixed typo: changed 'wai_time' to 'wait_time'

# Calculate the time when the alarm will go off, using modulo to ensure it wraps around after 23
time_when_alarm_go_off = (time + wait_time) % 24  # Use modulo to handle times past 23

# Print the calculated time when the alarm goes off
print("The alarm will go off at:", time_when_alarm_go_off)
