#!/usr/bin/python3
"""Checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specific class."""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specific class."""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
