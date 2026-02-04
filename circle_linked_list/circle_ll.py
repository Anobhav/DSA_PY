class Node:
    def __init__(self,val=None):
        self.val=val
        self.prev=None
        self.next=None
    
class circle_ll:
    def __init__(self):
        self.head=None
    
    def insert_at_ends(self,val):
        t=Node(val)
        if(self.head is None):
            self.head=t
            t.next=t
            return
        temp=self.head
        while(temp.next!=self.head):
            temp=temp.next
        t.next=self.head
        temp.next=t

    def insert_at_start(self,val):
        t=Node(val)
        if(self.head is None):
            self.head=t
            t.next=t
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        t.next = self.head
        temp.next = t
        self.head = t

    def _insert_after_pos(self, val, pos):
        t = Node(val)

        temp = self.head
        count = 1

        while count < pos - 1 and temp.next != self.head:
            temp = temp.next
            count += 1

        if count != pos - 1:
            print("Invalid position")
            return

        t.next = temp.next
        temp.next = t
