#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 12, 2025

# a program that asks the user for the number of sides,
# the length of the side, the color of the line, and the fill color of a regular polygon. 

import turtle

# Function to draw and fill a polygon
def draw_polygon(sides, length, line_color, fill_color):
    # Set up the turtle window
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Create a turtle object
    polygon = turtle.Turtle()

    # Set the line color
    polygon.pencolor(line_color)
    
    # Set the fill color
    polygon.fillcolor(fill_color)

    # Start filling the polygon
    polygon.begin_fill()

    # Calculate the angle between the sides
    angle = 360 / sides

    # Draw the polygon
    for _ in range(sides):
        polygon.forward(length)
        polygon.left(angle)

    # Finish filling the polygon
    polygon.end_fill()

    # Hide the turtle after drawing
    polygon.hideturtle()

    # Keep the window open
    turtle.done()

# Get user input
sides = int(input("Enter the number of sides of the polygon: "))
length = int(input("Enter the length of each side: "))
line_color = input("Enter the line color: ")
fill_color = input("Enter the fill color: ")

# Call the function to draw and fill the polygon
draw_polygon(sides, length, line_color, fill_color)

