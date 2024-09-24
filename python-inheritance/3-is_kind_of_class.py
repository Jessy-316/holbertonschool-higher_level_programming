#!/usr/bin/python3
"""Checks if an object is an instance of,
    or an instance of an inherited class from."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of,
    or an instance of an inherited class from."""
    if isinstance(obj, a_class):
        return True
    return False
