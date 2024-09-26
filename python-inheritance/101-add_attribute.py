#!/usr/bin/python3
"""Function that adds a new attribute to an object if it's possible."""


def add_attribute(object, attribute_name, value):
    """Adds a new attribute to an object if possible.
    
    Args:
        object: The object to which the attribute will be added.
        attribute_name: The name of the attribute to add.
        value: The value of the attribute to add.

    Raises:
        TypeError: If the object can't have a new attribute.
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(object, attribute_name, value)
