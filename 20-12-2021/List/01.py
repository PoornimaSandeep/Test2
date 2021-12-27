print("Remove specified index from list and print")
list1=[1,2,3,45,"fkjfk","4995.0"]
id=int(input("enter the index which you want to delete"))

print("1.using built in function")
for i in range(len(list1)):
    if i==id:
        list1.pop(i)
print(list1)



