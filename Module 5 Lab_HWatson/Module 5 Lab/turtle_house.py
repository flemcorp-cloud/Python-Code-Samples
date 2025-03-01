#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 12, 2025

import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("skyblue")  # Set the background to sky blue

# Create a turtle object
house = turtle.Turtle()
house.speed(5)  # Set a moderate speed for drawing
house.width(2)

# Function to draw a square (the house base)
def draw_square(color, size):
    house.begin_fill()
    house.fillcolor(color)
    for _ in range(4):
        house.forward(size)
        house.left(90)
    house.end_fill()

# Function to draw a triangle (the roof)
def draw_triangle(color, size):
    house.begin_fill()
    house.fillcolor(color)
    for _ in range(3):
        house.forward(size)
        house.left(120)
    house.end_fill()

# Draw the house
house.penup()
house.goto(-100, -100)  # Position the turtle
house.pendown()
draw_square("yellow", 200)  # Draw the base of the house

# Draw the roof
house.penup()
house.goto(-120, 100)  # Position for the roof
house.pendown()
draw_triangle("red", 240)  # Draw the roof

# Draw the door
house.penup()
house.goto(-30, -100)  # Position for the door
house.pendown()
house.begin_fill()
house.fillcolor("brown")
for _ in range(2):
    house.forward(40)
    house.left(90)
    house.forward(80)
    house.left(90)
house.end_fill()

# Draw windows
house.penup()
house.goto(-80, 20)  # Position for the first window
house.pendown()
house.begin_fill()
house.fillcolor("lightblue")
for _ in range(4):
    house.forward(40)
    house.left(90)
house.end_fill()

house.penup()
house.goto(40, 20)  # Position for the second window
house.pendown()
house.begin_fill()
house.fillcolor("lightblue")
for _ in range(4):
    house.forward(40)
    house.left(90)
house.end_fill()

# Hide the turtle after drawing
house.hideturtle()

# Finish drawing
turtle.done()


