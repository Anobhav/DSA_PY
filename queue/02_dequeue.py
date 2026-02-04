class Dequeue:

    def __init__(self):
        self.q=[]
    
    def is_empty(self):
        return len(self.q) == 0

    def insert_at_end(self,value):
        self.q.append(value)
    def insert_at_beg(self,value):
        self.q.insert(0,value)
    def pop_at_end(self):
        if self.is_empty():
            return
        return self.q.pop()
    def pop_in_front(self):
        if self.is_empty():
            return
        return self.q.pop(0)
q=Dequeue()
q.insert_at_beg(10)
q.insert_at_beg(2)
q.insert_at_end(30)
print(q.pop_in_front())
print(q.pop_at_end())
print(q.pop_in_front())
print(q.pop_in_front())