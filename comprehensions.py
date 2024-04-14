x = int(input("Enter X : "))
y = int(input("Enter Y : "))
z = int(input("Enter Z : "))
n = int(input("Enter n : "))
output = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            temp = []
            if(i+j+k == n):
                pass
            else:
                temp.append(i)
                temp.append(j)
                temp.append(k)
                output.append(temp)
print(output)







# Problem Statment 
# Problem 1
# Let's learn about list comprehensions! You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k is not equal to n. Here,0 <= i <= x; 0 <= j <= y; 0 <= k <= z Please use list comprehensions rather than multiple loops, as a learning exercise.
# Example
# x = 1
# y = 1
# z = 2
# n = 3
# All permutations of i, j, k] are:
# [ [0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2] ,[1 ,1,1]
# Print an array of the elements that do not sum to n = 3 [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]