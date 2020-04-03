class Node :
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack :
    def __init__(self):
        self.first = Node(None)
        self.N = 0
    
    def isEmpty(self):
        return self.first == None
    
    def get_size(self):
        return self.N 

    def push(self,x) :
        self.old = self.first
        self.first = Node(x)
        self.first.next = self.old
        self.N += 1
        print("Push : ",x)
    
    def pop(self) :
        self.old = self.first
        self.first = self.old.next
        self.N -= 1
        print("Pop : ", self.old.item)


s = Stack()
s.push("a")
s.push("b")
s.pop()
    


