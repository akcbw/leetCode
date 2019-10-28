class MyStack:
    def __init__(self):
        self.stackItems = []

    def pop(self):
        self.stackItems.pop()

    def push(self,item):
        self.stackItems.append(item)

    def peek(self):
        return None if (len(self.stackItems) == 0) else self.stackItems[-1]

    def isEmpty(self):
        return len(self.stackItems) == 0

    def size(self):
        return len(self.stackItems)

    def printStack(self):
        print(self.stackItems)
