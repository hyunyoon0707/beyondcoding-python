class Deque:
    def __init__(self):
        self.items = []
    
    def push_left(self, item):
        self.items.insert(0,item)
    
    def pop_left(self):
        return self.items.pop(0)
    
    def peek_left(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.size() == 0

    def push_right(self, item):
        self.items.append(item)
    
    def pop_right(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]

deque = Deque()

for i in range(3):
    deque.push_left(input())

while not deque.isEmpty():
    print(deque.pop_left())
    
    
    
   
