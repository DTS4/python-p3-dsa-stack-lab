class Stack:
    def __init__(self, items=None, limit=100):
        self.items = items if items is not None else []
        self.limit = limit

    def isEmpty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def push(self, item):
        """Add an item to the top of the stack if there is space."""
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            pass  # Avoid raising an error; do nothing if the stack is full.

    def pop(self):
        """Remove and return the top item from the stack."""
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None  # Return None instead of raising an error.

    def peek(self):
        """Return the top item from the stack without removing it."""
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None  # Return None instead of raising an error.

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

    def full(self):
        """Check if the stack is full."""
        return len(self.items) == self.limit

    def search(self, target):
        """Find the distance from the top of the stack to the target item."""
        try:
            # Find the index of the target in the reversed list
            distance = self.items[::-1].index(target)
            return distance
        except ValueError:
            return -1
