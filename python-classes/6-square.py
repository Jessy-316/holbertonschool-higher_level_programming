#!/usr/bin/python3
"""This module defines a Square class for representing squares."""


class Square:
    """Represents a square with a private size attribute.

    Attributes:
        __size (int): The size of the square's sides (must be >= 0).
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square instance with size validation.

        Args:
            size (int, optional):
            The size of the square's sides, Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

        error = "position must be a tuple of 2 positive integers"
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError(error)
        for number in position:
            if not isinstance(number, int) or number < 0:
                raise TypeError(error)
        self.__position = position

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter for the size attribute.

        Returns:
            int: The size of the square's sides.
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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square"""
        error = "position must be a tuple of 2 positive integers"
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(error)
        for number in value:
            if not isinstance(number, int) or number < 0:
                raise TypeError(error)
        self.__position = value

    def my_print(self):
        """Prints a square using the '#' character based on its size.

        If the size is 0, an empty line is printed. Otherwise, the square
        is printed with the side length corresponding to the size attribute,
        offset by the position attribute.
        """
        if self.__size == 0:
            print()
            return

        [print() for _ in range(self.__position[1])]

        for index in range(self.__size):
            print("_" * self.__position[0], end="")
            print("#" * self.__size)

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
