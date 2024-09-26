#!/usr/bin/python3
"""MyInt class that inherits from int."""


class MyInt(int):
    """A rebel integer class with inverted equality operators."""

    def __eq__(self, other):
        """Inverts the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the != operator."""
        return super().__eq__(other)
