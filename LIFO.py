class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
class LinkedList :
    def __init__(self):
        self.head = None
    def Display(self):
        printval = self.head
        if self.head == None:
            print("List is empty")
        else:
            while printval is not None:
                print(printval.data , end=" , ")
                printval = printval.next
            print()
    def POP(self):
        print("Deleting first element ")
        if self.head == None:
            print("List is empty deletion is not possible ")
        else:
            self.head = self.head.next
            
    def dellast(self):
        print("Deleting last element ")
        if self.head == None:
            print("List is empty deletion is not possible ")
        elif self.head.next is None:
            temp = self.head
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            print("Deleting ",temp.data)
            temp.next = None

    def PUSH(self,n):
        newNode = Node(n)
        newNode.next = self.head
        self.head = newNode

    def InsertAtEnd(self , n):
        newNode = Node(n)
        if self.head is None :
            self.head = newNode
        else:
            temp = self.head
            while(temp.next is not None):
                temp = temp.next
            temp.next = newNode

    def reverse_llist(self, llist):
        before = None
        current = llist.head
        if current is None:
            return
        after = current.next
        while after:
            current.next = before
            before = current
            current = after
            after = after.next
        current.next = before
        llist.head = current


l = LinkedList()
while True:
    print("_______________________")
    print("1 to insert \n2 to delete \n3 to diplay\n4.Reverse \n5 to exit")
    ch = int(input("Enter choice : "))
    if ch==1:
        print("     1 PUSH ")
        a = int(input("Enter choice : "))
        data = int(input("Enter data to be enter : "))
        if a == 1:
            l.PUSH(data)
    elif ch == 2:
        if l.head == None:
            print("List is empty deletion not possible ")
        else:
            print("     1.POP ")
            a = int(input("Select choice : "))
            if a == 1:
                l.POP()
    elif ch == 3:
        l.Display()
    elif ch == 4:
        l.reverse_llist(l)
        l.Display()
    elif ch == 5:
        break
    else:
        print("Invalid Choice ")