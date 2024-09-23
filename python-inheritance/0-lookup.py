#!/usr/bin/python3
"""
This module contains a single function `lookup` that retrieves a list of
available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj (any): The object to inspect.

    Returns:
        list: A list of attributes and methods available for the given object.
    """
    return dir(obj)
