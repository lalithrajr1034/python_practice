# print minimum value and append value and topmost value 
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push to min_stack if it's empty or new value is <= current min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return None
minStack = MinStack()
minStack.push(5)
minStack.push(3)
minStack.push(7)
print(minStack.getMin())  
minStack.pop()
print(minStack.top())  
print(minStack.getMin())  
minStack.pop()
print(minStack.getMin()) 
        