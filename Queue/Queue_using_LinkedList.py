class Node:
    '''
        creat Node
    '''
    def __init__(self,data=0) -> None:
        self.data = data
        self.next = None
class Queues:
    def __init__(self):
        self.font = None
        self.back = None
    def is_Empty(self):
        return self.font == None
    def enqueue(self,data):
        temp = Node(data)
        if self.is_Empty():
            self.font = temp
            self.back = temp
            return 
        self.back.next = temp 
        self.back = temp
    def dequeue(self):
        if self.is_Empty():
            print("Can't dequeue , ur queue is empty")
            return None
        element_dequeue = self.font.data
        self.font = self.font.next
        return element_dequeue
    def peek(self):
        return self.font.data