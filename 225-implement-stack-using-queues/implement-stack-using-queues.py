class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []


    def push(self, x: int) -> None:
        self.q1.append(x)


    def pop(self) -> int:

        # Move everything except the last element to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1[0])
            self.q1.pop(0)

        # Last element is the stack top
        x = self.q1[0]
        self.q1.pop(0)

        # Move everything back
        while len(self.q2) > 0:
            self.q1.append(self.q2[0])
            self.q2.pop(0)

        return x


    def top(self) -> int:

        # Move everything except the last element to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1[0])
            self.q1.pop(0)

        # Last element is the stack top
        x = self.q1[0]

        # IMPORTANT: top() should NOT remove it
        # So put this element into q2 as well
        self.q2.append(self.q1[0])
        self.q1.pop(0)

        # Move everything back to q1
        while len(self.q2) > 0:
            self.q1.append(self.q2[0])
            self.q2.pop(0)

        return x


    def empty(self) -> bool:

        if self.q1:
            return False

        return True