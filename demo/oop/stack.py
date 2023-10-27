class Stack:
    def __init__(self, limit=0):
        self.data = []
        self.limit = limit

    def push(self, value):
        if self.limit != 0 and self.length == self.limit:
            raise ValueError("Stack Full")

        self.data.append(value)

    def pop(self):
        if self.length == 0:
            raise ValueError("Stack Empty!")

        return self.data.pop()

    def peek(self):
        if self.length  == 0:
            raise ValueError("Stack Empty!")

        return self.data[-1]

    def clear(self):
        self.data.clear()

    @property
    def length(self):
        return len(self.data)


s = Stack(2)
#print(s.pop())
s.push('Python')
s.push('Java')
s.push("JS")

print(s.peek())
print(s.pop())
print(s.length)
