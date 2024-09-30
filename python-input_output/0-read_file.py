#!/usr/bin/python3
"""Python executable file."""


def read_file(filename=""):
    """Function that readsa text file and prints it to stdout."""
    with open(filename, 'r', encoding="utf-8") as file:
        read_data = file.read()
        print(read_data, end="")
