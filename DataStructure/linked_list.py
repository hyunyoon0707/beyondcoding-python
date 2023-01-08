class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = Node(None)
    
    def push(self,data):
        cur = self.head
        
        while cur.next:
            cur = cur.next
        
        cur.next = Node(data)
    
    def pop(self):
        cur = self.head
        before = None
        while cur.next:
            before = cur
            cur = cur.next
        data = cur.data
        before.next = None
        return data
    
    def size(self):
        cur = self.head
        s = 0
        while cur.next:
            s += 1
            cur = cur.next
        
        return s


linkedlist = LinkedList()
linkedlist.push(1)
linkedlist.push(2)
linkedlist.push(3)
print(linkedlist.pop())
print(linkedlist.size())






