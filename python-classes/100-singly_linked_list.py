#!/usr/bin/python3
"""Defines a node of a singly linked list"""


class Node():
    def __init__(self, data, next_node=None):
        """Initializes the Node with data and next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data, ensuring it's an integer"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node, ensuring it's either None or a Node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList():
    """Defines a singly linked list"""
    def __init__(self):
        """Initializes the linked list with an empty head"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position
        (increasing order)"""
        new_node = Node(value)

        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node is not None and
                    current.next_node.data < value):
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Prints the entire list, one node number per line"""
        current = self.__head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
