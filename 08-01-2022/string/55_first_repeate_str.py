"""
find the first repeated word in a given string
"""
str=input("Enter the string :")

words=str.split()
print(words)

flag=0
for word in words:
    count = 0
    for j in words:
        if j==word:
            count +=1
        if count == 2:
            flag=1
            print("first repeated word", word)
            break
    if flag==1:
        break
