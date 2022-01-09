print("Frequency of elements")
l=[1,23,45,34,12,33,1,23,1,45,12,23]
dict={}

for i in l:
    if i not in dict:
        dict[i]=1
    elif i in dict:
        dict[i]+=1


print(dict)