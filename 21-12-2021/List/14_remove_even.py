print("Remove even elements and print list")
lst=[2,3,46,89,67,36,90,34]

print("1.algorithm")
lst2=[]
for i in lst:
    if i%2==0:
        lst2.append(i)
print(lst2)

print("2.userdeined function")
def even_ele(l):
    lst2 = []
    for i in lst:
        if i % 2 == 0:
            lst2.append(i)
    return lst2
ls=even_ele(lst)
print(ls)

