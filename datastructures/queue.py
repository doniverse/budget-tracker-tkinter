
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        # Create a new node
        new_node = Node(value)
        
        # If queue is empty, set 
        # new node as front and rear
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            # If queue is not empty,
            # add new node at the rear
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        # Check if queue is empty
        if self.front is None:
            print("Queue is empty, cannot dequeue")
            return None
        else:
            # dequeue the front element
            temp = self.front
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return temp.data
        
    def peek(self):
        if self.front:
            return self.front.data['amount']
        else:
            return None

