class Node:
    def __init__(self, val, next=None):
        self.data = val
        self.next = next


class singlelinkedlist:
    def __init__(self, head=None):
        self.head = head

    def insertatbeg(self, val):
        temp = Node(val)
        temp.next = self.head
        self.head = temp

    def insertatend(self, val):
        temp = Node(val)
        if self.head is None:
            self.head = temp
            return

        t1 = self.head
        while t1.next is not None:
            t1 = t1.next
        t1.next = temp

    def insert_at_middle(self, val, x):
        temp = self.head
        while temp is not None:
            if temp.data == x:
                newnode = Node(val)
                newnode.next = temp.next
                temp.next = newnode
                return
            temp = temp.next

    def deeltell(self, val):
        temp = self.head

        if temp is None:
            return

        if temp.data == val:
            self.head = temp.next
            return

        prev = None
        while temp is not None:
            if temp.data == val:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next

    def printll(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


obj = singlelinkedlist()
obj.insertatend(20)
obj.insertatend(40)
obj.insertatbeg(10)
obj.insert_at_middle(30, 20)
obj.deeltell(20)
obj.printll()
