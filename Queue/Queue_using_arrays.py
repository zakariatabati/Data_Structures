class Queue:
    def __init__(self,capacity):
        self.capacity = capacity
        self.data = [None]*self.capacity
        self.size = 0
        self.front =0
        self.back = 0
    def is_empty(self):
        return self.size == 0
    def is_full(self):
        return self.size == self.capacity
    
    def enqueue(self,data):
        if self.is_full():
            print("cant't queue , ur queue is full")
            return 
        self.data[self.back] = data 
        self.back = (self.back+1)%self.capacity
        self.size+=1
        
    def dequeue(self):
        if self.is_empty():
            print( "Can't dequeue , ur queue is empty")
            return 
        element_dequeue = self.data[self.front]
        self.front = (self.front +1)%self.capacity
        self.size-=1
        return element_dequeue

        
    def peek(self):
        return self.data[self.front]