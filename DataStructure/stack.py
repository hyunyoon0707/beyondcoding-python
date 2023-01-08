class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.size() == 0


stack = Stack()
x = list(map(int,input().split()))
for i in x:
    stack.push(i)
for i in range(stack.size()):
    print(stack.pop())

# while not stack.isEmpty():
#     print(stack.pop())









