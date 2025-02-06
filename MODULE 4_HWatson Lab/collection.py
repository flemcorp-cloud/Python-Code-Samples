#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 5, 2025

# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870
# William Thackeray died in 1863
# Anthony Trollope died in 1882
# Gerard Manley Hopkins died in 1889


# Dictionary storing authors and their year of death
authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
}

# Loop through dictionary items (key-value pairs)
for author, date in authors.items():  # Fixed incorrect syntax
    # Print formatted output using f-strings (cleaner and more readable)
    print(f"{author} died in {date}.")

