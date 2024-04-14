
def Insort(myarr):
    for i in range(1 , len(myarr)):
        t = myarr[i]
        j = i-1
        while j >= 0 and t < myarr[j]:
            myarr[j + 1] = myarr[j]
            j = j-1
        myarr[j+1] = t
    return myarr

myarr = [10,20,3,1,45,56,2]
print(myarr)
Insort(myarr)
print("Sorted list")
print(myarr)
