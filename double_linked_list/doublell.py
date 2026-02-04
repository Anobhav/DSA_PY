class Node:
    def __init__(self, val=None):
        self.val=val
        self.next=None
        self.prev=None

class doublell:
    def __init__(self):
        self.head=None

    def insertatend(self, val):
        t=Node(val) 
        if self.head == None:
            self.head=t
            return

        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=t
            t.prev=temp
    
    def insertatbeg(self,val):
        t=Node(val)
        if self.head==None:
            self.head=t
            return
        else:
            self.head.prev=t
            t.next=self.head
            self.head=t
    def printdll(self):
        t=self.head
        while(t != None):
            print(t.val, end=" <--> ")
            t=t.next
    
    def insertionatmid(self,value,x):
        t=self.head
        while(t.val!=None):
            if(t.val==x):
                break
            else:
                t=t.next
            
        temp=Node(value)
        temp.next=t.next
        t.next.prev=temp
        t.next=temp
        temp.prev=t
    def delete(self,value):
        if(self.head==None):
            print('empty')
            return
        t=self.head
        if(t.val==value):
            self.head=t.next
            self.head.prev=None
            return
        
        while(t.next!=None):
            if(t.val==value):
                t.prev.next=t.next
                t.next.prev=t.prev
                return
            else:
                t=t.next

        if(t.val==value):
            t.prev.next=None

obj=doublell()
obj.insertatend(10)
obj.insertatend(20)
obj.insertatend(30)
obj.insertatbeg(5)
obj.insertionatmid(25,20)
obj.delete(10)
obj.delete(25)
obj.delete(5)
obj.printdll()
