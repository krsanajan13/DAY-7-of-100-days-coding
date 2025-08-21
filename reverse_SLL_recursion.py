class Node:
    def __init__(self,val ):
        self.val=val
        self.next=None

class SingleLinkedList:
    def __init__(self):
        self.root=None

    def addNewNode(self,val):
        n=Node(val)
        if self.root==None:
            self.root=n
            return
        temp=self.root
        while temp.next!=None:
            temp=temp.next
        temp.next=n

    def print_reverse(self, node):
        if node is None:
            return
        self.print_reverse(node.next)
        print(node.val, end=" ")


    def reverse_display(self):
        print("Linked List in reverse order:")
        self.print_reverse(self.root)
        print()





s=SingleLinkedList()
s.addNewNode(10)
s.addNewNode(20)
s.addNewNode(30)
s.addNewNode(40)

s.reverse_display()
