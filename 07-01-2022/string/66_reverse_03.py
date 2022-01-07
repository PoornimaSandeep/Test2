"""
Reverse each word and reverse word again. Input
"""
str=input("Enter the input: ")
words=str.split()
l=[i[::-1] for i in words]

print("first reverse :")
for i in l:
    print(i,end=" ")
print("")
print("")
print("second reverse:" )
for i in l:
    print(i[::-1],end=" ")