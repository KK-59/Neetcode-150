class MinStack:

    def __init__(self):
        self.minimum = None
        self.minStack = []
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimum == None:
            self.minimum = val
        elif val <= self.minimum:
            self.minStack.append(self.minimum)
            self.minimum = val
        
    def pop(self) -> None:
        if self.minimum == self.stack[-1]:
            if len(self.minStack) > 0:
                self.minimum = self.minStack[len(self.minStack) - 1]
                self.minStack.pop()
            else:
                self.minimum = None 
        x = self.stack[:-1]
        if len(self.minStack) > 0 and x == self.minStack[-1]:
            self.minStack.pop()
            
        self.stack = self.stack[:-1]
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum
        
