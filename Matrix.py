class Matrixs:
    def __init__(self):
        self.r = int(input("Enter row : "))
        self.c = int(input("Enter column : "))
        self.matrix = []
        for i in range(self.r):
            print("Enter row ",i ," : ",end=' ')
            temp = []
            for j in range(self.c):
                h = int(input())
                temp.append(h)
            self.matrix.append(temp)

    def display(self):
        print("matrix is ")
        for i in range(self.r):
            print(self.matrix[i])

    def addition(self,second):
        if self.r == second.r and self.c == second.c:
            self.temp = []
            for i in range(self.r):
                a = []
                for j in range(self.c):
                    h = self.matrix[i][j] + second.matrix[i][j]
                    a.append(h)
                self.temp.append(a)
            print("Addition is ")
            for i in self.temp:
                print(i)
            return self.temp
        else:
            print("Addition not possible ")
            return None
    
    def subtraction(self,second):
        if self.r == second.r and self.c == second.c:
            self.temp = []
            for i in range(self.r):
                a = []
                for j in range(self.c):
                    h = self.matrix[i][j] - second.matrix[i][j]
                    a.append(h)
                self.temp.append(a)
            print("Subtracation is ")
            for i in self.temp:
                print(i)
            return self.temp
        else:
            print("Subtraction not possible ")
            return None
            
    def multiplication(self,second):
        if self.c == second.r :
            m = []
            for i in range(self.r):
                row = []
                for j in range(second.c):
                    t = 0
                    for k in range(self.c):
                       t += self.matrix[i][k]*second.matrix[k][j] 
                    row.append(t)
                m.append(row)
            print("Multiplication is ")
            for i in m:
                print(i)
            return m
        else:
            print("Multiplication not possible ")
            return None
                    

print("First Matrix")
a = Matrixs()
a.display()
print("Second Matrix")
b = Matrixs()
b.display()
while True:
    print("---------------------------------")
    print("1.Addition \n2.Subtraction \n3.Multiplication\n4.Display")
    print("5.Update first\n6.Update second\n7.Quit")
    ch = int(input("Select option : "))
    if ch == 1:
        a.addition(b)
    elif ch == 2:
        a.subtraction(b)
    elif ch== 3:
        a.multiplication(b)
    elif ch == 4:
        print("First matrix is ")
        a.display()
        print("Second matrix is ")
        b.display()
    elif ch == 5:
        a = Matrixs()
    elif ch == 6:
        b = Matrixs()
    elif ch == 7:
        break
    else:
        print("Andha he kya be ")
    