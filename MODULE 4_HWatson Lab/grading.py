#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 5, 2025

# A program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade,
# and a message stating whether the student is passing.

# Average Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.


# Get user input for three exam grades and ensure they are integers
exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: "))  # Fixed extra parenthesis
exam_three = int(input("Input exam grade three: "))  # Changed from str() to int()

# Store grades in a list
grades = [exam_one, exam_two, exam_three]  # Fixed missing commas and incorrect variable name

# Calculate the sum and average of grades
total = sum(grades)  # Used built-in sum() function 
avg = total / len(grades)  # Fixed typo in 'grades'

# Determine the letter grade based on average score
if avg >= 90:
    letter_grade = "A"
elif avg >= 80:  # No need to check "and avg < 90" since previous condition already handled it
    letter_grade = "B"
elif avg >= 70:  # Simplified condition
    letter_grade = "C"
elif avg >= 60:  # Simplified condition
    letter_grade = "D"
else:  # No need to specify "elif avg < 60"
    letter_grade = "F"

# Print individual exam grades
for grade in grades:
    print("Exam: " + str(grade))

# Print the average and letter grade
print("Average: " + str(avg))
print("Grade: " + letter_grade)

# Determine if the student is passing or failing
if letter_grade == "F":  # Fixed incorrect variable name and comparison operator
    print("Student is failing.")  # Fixed incorrect print syntax
else:
    print("Student is passing.")
