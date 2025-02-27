#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 27, 2025

# A program that will produce 5 nested blue squares.


import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range(4):  # Loop to draw 4 sides of a square
        t.forward(sz)  # Move forward by 'sz' units
        t.left(90)  # Turn left by 90 degrees

# Create a turtle screen
wn = turtle.Screen()

# Create a turtle named 'alex'
alex = turtle.Turtle()
alex.color("blue")  # Set the turtle color to blue

# Draw multiple squares with increasing sizes
size = 20  # Initial size of the smallest square
for _ in range(5):  # Draw 5 nested squares
    drawSquare(alex, size)  # Call the function to draw a square
    alex.penup()  # Lift the pen to reposition without drawing
    alex.backward(10)  # Move left to keep the squares centered
    alex.right(90)  # Turn down
    alex.forward(10)  # Move down to center the next square
    alex.left(90)  # Reset the direction
    alex.pendown()  # Lower the pen to draw again
    size += 20  # Increase the square size

# Close the window when clicked
wn.exitonclick()




