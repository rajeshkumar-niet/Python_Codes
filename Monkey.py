doors  = [  ]
status = 'Closed'
t = 1
for i in range(10):
    a = []
    for j in range(10):
        a.append(status)
    doors.append(a)
for i in range(10):
    print(doors[i])

for mon in range(1,11):
    for i in range(10):
        for j in range(10):
            if((i*10+j )%mon == 0 ):
                if doors[i][j] == 'Closed':
                    doors[i][j] = 'Open'
                else:
                    doors[i][j] = 'Closed'
    print("After Monkey ", mon)
    for i in range(10):
        print(doors[i])



print("After tesk ")
for i in range(10):
    print(doors[i])