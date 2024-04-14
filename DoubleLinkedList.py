class Node:
    def __init__(self , data = None ):
        self.prev = None
        self.data = data
        self.next = None

class Double_Link():
    def __init__(self):
        self.head = None
        self.tail = None
    def startin(self):
        data = int(input("Enter value to enter :  "))
        newnode = Node(data)
        newnode.next = self.head
        newnode.prev = None
        if self.head is not None:
            self.head.prev =  newnode
        self.head = newnode
    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data , end=" , ")
            temp = temp.next
        print()
    def inverseDisplay(self , a):
        temp = Double_Link()
        print(temp)
        temp = a
        print(temp)
        i = 0
        while temp.tail == None:
            print(i,"  ",temp.data , end=" , ")
            temp = temp.prev
        print()
            

dl = Double_Link()
while True:
    print("Select Oparation \n1.Insert at start")
    print("2.Insert at last\n3.Display")
    print("4.Display inversely ")
    ch = int(input("9.Quit  :  "))
    if ch == 1:
        dl.startin()
    elif ch == 2:
        dl.lastin()
    elif ch == 3:
        dl.display()
    elif ch == 4:
        a = dl
        dl.inverseDisplay(a)
    elif ch == 9:
        break