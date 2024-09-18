#!/usr/bin/python3
"""This module defines a Square class for representing squares."""


class Square:
    """Represents a square with a private size attribute.

    Attributes:
        __size (int): The size of the square's sides (must be >= 0).
    """

    def __init__(self, size=0):
        """Initializes a Square instance with size validation.

        Args:
            size (int, optional):
            The size of the square's sides, Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter for the size attribute.

        Returns:
            int: The size of the square's sides
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute with validation.

        Args:
            value (int): The new size of the square's sides.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Checks if the area of two squares are equal"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks if the area of two squares are not equal"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Checks if this square's area is less than another's"""
        return self.area() < other.area()

    def __le__(self, other):
        """Checks if this square's area is less than or equal to another's"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if this square's area is greater than another's"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if this square's area is greater than or equal to another's"""
        return self.area() >= other.area()

    def __str__(self):
        """String representation of the square."""
        return f"Square(size={self.size})"
