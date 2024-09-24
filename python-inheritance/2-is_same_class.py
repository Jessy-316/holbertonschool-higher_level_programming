#!/usr/bin/python3
"""Checks if an object is exactly an instance of a_class."""


def is_same_class(obj, a_class):
    """Checks if an obj is an instance of a_class."""
    return type(obj) is a_class
