# Week 1.6, Session 1: Task 3

import math
from point import Point

VALID_COLOURS = {"red", "orange", "yellow", "green", "blue", "purple"}


class Shape:
    """
    Superclass for different types of shape.
    """

    def __init__(self, position, colour):
        """
        Creates a shape with the specified position & colour.
        """
        self.set_position(position)
        self.set_colour(colour)

    def set_position(self, position):
        """
        Moves this shape to the given position.
        """
        if not isinstance(position, Point):
            raise TypeError("position must be a Point")

        self.position = position

    def set_colour(self, colour):
        """
        Sets this shape's colour to the given colour.
        """
        if colour not in VALID_COLOURS:
            raise ValueError(f"invalid color: must be one of {VALID_COLOURS}")

        self.colour = colour


class Circle(Shape):
    """
    A circle, with a radius, position and colour.
    """

    def __init__(self, radius, position, colour="red"):
        """
        Creates a circle with the given radius, position & colour.
        """
        super().__init__(position, colour)
        self.set_radius(radius)

    def set_radius(self, radius):
        """
        Sets the radius of this circle.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")

        if radius <= 0:
            raise ValueError("radius must be greater than zero")

        self.radius = radius

    def __str__(self):
        """
        Returns a string representation of this circle.
        """
        return f"{self.colour} circle, radius {self.radius}, at {self.position}"

    def area(self):
        """
        Returns the area of this circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Returns the perimeter (circumference) of this circle.
        """
        return 2 * math.pi * self.radius
