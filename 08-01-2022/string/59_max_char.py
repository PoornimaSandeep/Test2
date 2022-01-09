"""
 find the maximum occurring character in a given string
"""
str=input("Enter the number :")
dict={}

for i in str:
    count = 0
    for j in str:
        if i==j:
            count +=1
    dict[i]=count

print(dict)
max=max(dict.values())
for i, j in dict.items():
    if j==max:
        print("maximum occurring character is :", i)


