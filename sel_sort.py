def Sel_Sort(myarr):
    for i in range(len(myarr)):
        mini = i
        for j in range(i,len(myarr)):
            if myarr[j]<myarr[mini]:
                mini = j
        myarr[i] , myarr[mini] = myarr[mini] , myarr[i]
      
a = [10,20,3,1,5,60,1,200]
print(a)
Sel_Sort(a)
print(a)
