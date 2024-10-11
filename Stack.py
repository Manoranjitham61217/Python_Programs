class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")

    def size(self):
        return len(self.items)


# Example usage:
if __name__ == "__main__":
    stack = Stack()

    stack.push("a")
    stack.push("b")
    stack.push("c")

    print("Stack:", stack.items)
    print("Number of items in stack", stack.size())
    print("The top value in the stack is:", stack.peek())

    value_popped = stack.pop()
    print("Value removed from Stack:", value_popped)
    print("Remaining elements in Stack are:", stack.items)
