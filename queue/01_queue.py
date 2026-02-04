class Queue:
    def __init__(self):
        self.q=[]
    
    def is_empty(self):
        if len(self.q) == 0:
            return "Queue is empty"
        
    def insert(self,value):
        self.q.append(value)

    def pop(self):
        if self.is_empty():
            return self.is_empty()
        return self.q.pop(0)

q=Queue()
q.insert(10)
q.insert(20)
q.insert(30)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())