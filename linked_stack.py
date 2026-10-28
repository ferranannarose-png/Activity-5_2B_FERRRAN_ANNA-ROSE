class Node:
    """One node in a singly linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedStack:
    """Stack implemented using a linked list."""

    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def is_full(self):
        # A linked stack has no fixed capacity.
        return False

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack.")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: there is no top element.")
        return self.top.value

    def state(self):
        values = []
        current = self.top
        while current is not None:
            values.append(current.value)
            current = current.next
        return values
