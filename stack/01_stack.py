class stack:
    def __init__(self):
        self.s=[]

    def length(self):
        return len(self.s)
    
    def push(self,value):
        self.s.append(value)
    
    def peek(self):
        if len(self.s) == 0:
            raise Exception("stack is empty")
    
        else:
            return self.s[-1]
        
    def pop(self):
        if len(self.s)==0:
            raise Exception("stack is empty")
        else:
            return self.s.pop(-1)
    
stk=stack()
stk.push(10)
stk.push(15)
print(stk.peek())
stk.pop()
print(stk.peek())
stk.pop()
print(stk.peek())