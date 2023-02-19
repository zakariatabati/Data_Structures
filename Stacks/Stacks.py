class Stacks:
    def __init__(self,capacity) -> None:
        self.capacity = capacity
        self.data = [None]*self.capacity
        self.top = -1
        
    def is_full(self) -> bool:
        return self.capacity == self.top -1
        
    def is_Empty(self) -> bool:
        return self.top == -1

    def push(self,data) -> None:
        if self.is_full():
            return " The Stacks is Full. Can't push"   
        self.top = self.top+1
        self.data[self.top] = data 

    def pop(self) -> int:
        if self.is_Empty():
            return "Your Stacks is Empty Can't pop "
        temp = self.data[self.top]
        self.top = self.top -1
        return temp
        
    def peek(self) -> int :
        if self.is_Empty():
            return "Your Stacks is Empty Can't peek "
        return self.data[self.top]
        
    def __str__(self) -> str:
        return str(self.data)
