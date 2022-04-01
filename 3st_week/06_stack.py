from dataclasses import dataclass


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.head = None
    
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty!"
        delete_head = self.head
        self.head = self.head.next
        return delete_head


    def peek(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.head.data
    
    def is_empty(self):
        return self.head is None

stack = Stack()
stack.push(3)
print(stack.peek())
stack.push(4)
print(stack.peek())
print(stack.pop().data)
print(stack.peek())
print(stack.pop().data)
print(stack.is_empty())