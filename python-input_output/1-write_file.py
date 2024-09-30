#!/usr/bin/python3
"""Python executable file."""


def write_file(filename="", text=""):
    """Function that writes a string to a text file
    and returns the number of characters written."""
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
