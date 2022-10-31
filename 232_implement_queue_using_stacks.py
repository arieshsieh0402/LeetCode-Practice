class MyQueue:

    def __init__(self):
        self.stack = []
        self.temp_stack = []
        self.first_val = None

    def push(self, x: int) -> None:
        if not self.stack:
            self.first_val = x
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return None
        elif len(self.stack) == 1:
            return self.stack.pop()
        while len(self.stack) > 1:
            self.first_val = self.stack.pop()
            self.temp_stack.append(self.first_val)
        result = self.stack.pop()
        self.first_val = self.temp_stack.pop()
        self.temp_stack.append(self.first_val)
        while self.temp_stack:
            self.stack.append(self.temp_stack.pop())
        self.temp_stack = []
        return result

    def peek(self) -> int:
        return self.first_val

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
