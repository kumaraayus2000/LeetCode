class MinStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, value: int) -> None:
        self.s1.append(value)

        if not self.s2 or value<=self.s2[-1]:
            self.s2.append(value)
        

    def pop(self) -> None:

        x = self.s1.pop()

        if x== self.s2[-1]:
            self.s2.pop()
        

    def top(self) -> int:
        return self.s1[-1]
        

    def getMin(self) -> int:
        return self.s2[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()