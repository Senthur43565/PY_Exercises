class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()

# Push elements onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Peek the top element
top_element = stack.peek()
print("Top element:", top_element)  # Output: Top element: 3

# Pop elements from the stack
popped_element = stack.pop()
print("Popped element:", popped_element)  # Output: Popped element: 3

# Check if the stack is empty
print("Is the stack empty?", stack.is_empty())  # Output: Is the stack empty? False

# Get the size of the stack
stack_size = stack.size()
print("Stack size:", stack_size)  # Output: Stack size: 2
