class Stack_Iterator:
    def __init__(self, data):
        self.data = data
        self.pos = len(data) - 1

    def __next__(self):
        if self.pos >= 0:
            self.pos -= 1
            return self.data[self.pos + 1]
        else:
            raise StopIteration()

class Stack:
    def __init__(self, limit=0):
        self.data = []
        self.limit = limit

    def __iter__(self):
        return  Stack_Iterator(self.data)

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


s = Stack(6)
#print(s.pop())
s.push('Python')
s.push('Java')
s.push("JS")

# print(s.peek())
# print(s.pop())
# print(s.length)

for v in s:
    print(v)
