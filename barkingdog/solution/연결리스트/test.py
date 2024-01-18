from collections import deque

class LinkedList:

    def __init__(self):
        self.linked_list = deque()

    def append(self, value):
        self.linked_list.append(value)

    def prepend(self, value):
        self.linked_list.appendleft(value)

    def insert(self, idx, value):
        self.linked_list.insert(idx, value)

    def pop(self):
        return self.linked_list.pop()
    
    def popleft(self):
        return self.linked_list.popleft()
    
    def remove(self, value):
        try:
            self.linked_list.remove(value)
        except ValueError:
            return -1

    def index(self, value):
        try:
            return self.linked_list.index(value)
        except ValueError:
            return -1
        
    def display(self):
        print(list(self.linked_list))
        
    
Llist = LinkedList()
Llist.append(1)
Llist.append(3)
Llist.append(4)
Llist.prepend(2)
Llist.insert(2, 10)
Llist.remove(2)
Llist.display()
print(Llist.index(7))

            
