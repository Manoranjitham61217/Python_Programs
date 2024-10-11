class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None
    
    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def precedence(self,op):
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        if op == '^':
            return 3
        return 0

    def is_operand(self,ch):
        return ch.isalpha() or ch.isdigit()

    def infix_to_postfix(self,expression):
        stack = LinkedListStack()
        output = [] 
    
        for char in expression:
            if self.is_operand(char):
                output.append(char)
            elif char == '(':
                stack.push(char)
            elif char == ')':
                while not stack.is_empty() and stack.peek() != '(':
                    output.append(stack.pop())
                stack.pop()
        
                while (not stack.is_empty() and self.precedence(stack.peek()) >= self.precedence(char)):
                    output.append(stack.pop())
                stack.push(char)
    
    
        while not stack.is_empty():
            output.append(stack.pop())
    
    
        return ''.join(output)

ip=LinkedListStack()
str="(a+b)*(c-b)"
print(ip.infix_to_postfix(str))
