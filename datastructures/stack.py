

class Node: 
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self) -> None:
        self.head = None
        
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
    
    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped
    
    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data
    
    # def __str__(self):
    #     printString = ''
    #     while(self.next):
    #         printString += self.data
    #     return printString
    
