from ast import Delete
class Queue:
    def __init__(self) -> None:
        self.arr = []
        
    def insert(self ):
        temp = int(input("Enter the element to insert : "))
        self.arr.append(temp)
    def delete(self ):
        if self.arr == []:
            print("Queue is empty deletion not possible")
        else:
            self.arr.pop()
    def show(self):
        print(self.arr)
    def IsEmpty(self):
        if self.arr == []:
            print("Enter Queue is Empty ")
        else:
            print("Queue is Not Empty")
            
print("Welcome to Stack ")
q = Queue()
ch = 1
while ch != 5:
    print("----------------------------------------------")
    print("1 for insert ")
    print("2 for delete ")
    print("3 for display ")
    print("4 to check whether queue is empty or not")
    print("5 for exit ")
    ch = int(input("Enter your choice "))
    if ch == 1:
        q.insert()
    elif ch == 2 :
        q.delete()
    elif ch == 3 :
        q.show()
    elif ch == 4:
        q.IsEmpty()
    elif ch == 5:
        break
    else :
        print("Aandha he kya...........")