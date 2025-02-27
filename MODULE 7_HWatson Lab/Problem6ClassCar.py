#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: February 26, 2025

#  A program that defines a Car class with attributes such as model, year, color, 
#  type, and manufacturer. It includes methods to retrieve each attribute 
#  and a method (fullspecs) to return the complete car specifications.

class Car:
    """A class to represent a car with attributes and methods."""
    
    def __init__(self, model, year, color, car_type, manufacturer):
        """Initialize car attributes."""
        self.model = model
        self.year = year
        self.color = color
        self.car_type = car_type  # New attribute: type of car (e.g., SUV, Sedan, etc.)
        self.manufacturer = manufacturer  # New attribute: Manufacturer (e.g., Toyota, Ford)
    
    # Getter methods
    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_type(self):
        return self.car_type  # New method to return car type

    def get_manufacturer(self):
        return self.manufacturer  # New method to return manufacturer

    # Method to return full specifications of the car
    def fullspecs(self):
        return f"{self.manufacturer} {self.model} ({self.car_type}) - {self.year}, {self.color}"

# Creating car objects with additional attributes
car1 = Car("Sports", 2012, "Blue", "Coupe", "Ferrari")
car2 = Car("Sedan", 2020, "Black", "Luxury", "Mercedes-Benz")

# Printing attribute values using getter methods
print(car1.get_color())        # Output: Blue
print(car1.get_model())        # Output: Sports
print(car2.get_color())        # Output: Black
print(car1.get_type())         # Output: Coupe
print(car2.get_manufacturer()) # Output: Mercedes-Benz

# Printing full specifications
print(car1.fullspecs())        # Output: Ferrari Sports (Coupe) - 2012, Blue
print(car2.fullspecs())        # Output: Mercedes-Benz Sedan (Luxury) - 2020, Black
