# Given two strings. The task is to check whether the given strings are anagrams of each other or not. 

# # An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, “abcd” and “dabc” are an anagram of each other.
str1 = input("Enter first string : ")
str2 = input("Etner second string : ")
temp1 = []
for i in str1:
    if(i not in temp1):
        temp1.append(i)
temp1.sort()

temp2 =[]
for i in str2:
    if(i not in temp2):
        temp2.append(i)
temp2.sort()

if(temp1 == temp2):
    print("given strings are anagrams of each other")
else:
    print("given strings are not anagrams of each other")