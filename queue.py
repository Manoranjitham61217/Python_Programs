class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None  # The front of the queue (where we dequeue)
        self.rear = None   # The rear of the queue (where we enqueue)
    
    def isEmpty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:  # If queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def dequeue(self):
        if self.isEmpty():
            return None
        temp = self.front
        self.front = temp.next
        # If the front becomes None, set rear to None as well
        if self.front is None:
            self.rear = None
        return temp.data
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.front.data
    
    def size(self):
        count = 0
        temp = self.front
        while temp:
            count += 1
            temp = temp.next
        return count

# Test the queue
queue = Queue()
for i in range(int(input())):
    command = input().split()
    if command[0] == "enqueue":
        queue.enqueue(int(command[1]))
    elif command[0] == "dequeue":
        print(queue.dequeue())
    elif command[0] == "peek":
        print(queue.peek())
    elif command[0] == "isEmpty":
        print(queue.isEmpty())
    elif command[0] == "size":
        print(queue.size())
    else:
        break
