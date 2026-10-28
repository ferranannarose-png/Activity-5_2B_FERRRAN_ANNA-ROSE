class Node:
    """One node in a singly linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedQueue:
    """Queue implemented using front and rear linked-list references."""

    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def is_full(self):
        # A linked queue has no fixed capacity.
        return False

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
        else:
            self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from an empty queue.")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty: there is no front element.")
        return self.front.value

    def state(self):
        values = []
        current = self.front
        while current is not None:
            values.append(current.value)
            current = current.next
        return values
