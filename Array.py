import array as ar 
myarr = ar.array('l' , [] )

def show(myarr):
        print("Array is : ")
        for i in myarr:
            print(i , end=' ')
        print()
        
# Linear Search Code 
def Lsearch(arr):
    v = int(input("Enter Value to search : "))
    t = -1
    for i in range(len(arr)):
        if v == arr[i] :
            t = i
            break
            
    if t == -1:
        print("Element is not found")
    else:
        print("Element is found at " , i)

# Binery Search Code
def Bsearch(myarr):
    print("Bubble sort needed sorted list so we are sorting list")
    BubbleSort(myarr)
    show(myarr)
    v = int(input("Enter number to search : "))
    first = 0
    last = len(myarr)-1
    index = -1
    while ((first < last )and (index == -1)):
        print("Searching ")
        mid = (first+last)//2
        if v == myarr[mid]:
            index = mid 
        else:
            if v < myarr[mid] :
                last = mid-1
            else:
                first = mid+1
    print(index)
    if index == -1:
        print("Not found ")
    else:
        print("Element found at ",index )
    return index

# Bubble Sort 
def BubbleSort(myarr):
    l = len(myarr) 
    for i in range(l-1):
        for j in range(l-i-1):
            if myarr[j]>myarr[j+1]:
                myarr[j] , myarr[j+1] = myarr[j+1] , myarr[j]
    show(myarr)
    return myarr

# Insertion Sorting
def Insort(myarr):
    l = len(myarr)
    for i in range(1 , l):
        t = myarr[i]
        j = i-1
        while j>=0 and t<myarr[j]:
            myarr[j+1] = myarr[j]
            j = j-1
        myarr[j+1] = t
    return myarr

# Selection Sort 
def Sel_Sort(myarr):
    for i in range(len(myarr)):
        mini = i
        for j in range(i,len(myarr)):
            if myarr[j]<myarr[mini]:
                mini = j
        myarr[i] , myarr[mini] = myarr[mini] , myarr[i]
    show(myarr)
    


while True:
    print()
    print("---------------------------------------------")
    print("1.Insert \n2.Delete \n3.Display\n4.Search\n5.Sort \n6.Quit")
    ch = int(input("Enter Choice : "))
    if ch == 1:
        print("\t1.Insert at Start\n\t2.Insert at Last \n\t3.Insert at specific location ")
        a = int(input("Enter choice : "))
        if a == 1:
            temp = int(input("Enter value(Start) : "))
            myarr.insert(0 , temp)
        elif a  == 2:
            temp = int(input("Enter value(Last) : "))
            myarr.append(temp)
        elif a  == 3:
            temp = int(input("Enter value : "))
            v = int(input("Enter index value : "))
            myarr.insert(v , temp)
        else:
            print("Incorrect input")
        show(myarr)
    elif ch == 2:
        print("\t4.Delete front \n\t5.Delete last \n\t6.Delete by Index \n\t7.Delete by value")
        a= 0
        a = int(input("Enter choice : "))
        if a == 4:
            myarr.pop(0)
        elif a == 5:
            myarr.pop()
        elif a == 6 :
            v = int(input("Enter index : "))
            myarr.pop(v)
        elif a == 7:
            v = int(input("Enter value : "))
            myarr.remove(v)
        else:
            print("Incorrect Input")
        show(myarr)
    elif ch == 3:
        show(myarr)
    elif  ch == 4:
        a = int(input("\t1.Linear Search\n\t2.Binary Search\n"))
        show(myarr)
        if a == 1:
            Lsearch(myarr)
        elif a == 2:
            Bsearch(myarr)
        else:
            print("Invalid choice")
    elif ch == 5:
        show(myarr)
        a = int(input("\t1.Bubble sort\n\t2.Insertion sort\n\t3.Selection Sort\n "))
        if a==1:
            BubbleSort(myarr)
        elif a == 2:
            Insort(myarr)
        elif a == 3:
            Sel_Sort(myarr)
        else:
            print("Invalid choice")
        show(myarr)
    elif ch == 6:
        break
    else:
        print("!!!!!!!!!!!Enter correct option!!!!!!!!!!!")