print("Difference betweeen 2 lists")
lst1=[1,2,3,45,]
lst2=[4,5,3,98]
ls=lst1+lst2
new_lst=[i for i in ls if i not in lst1 or i not in lst2]
print(new_lst)

print("using userdefined function")

def differ_lst(l1,l2=[1,2,5,6,7]):
    new_lst=[]
    for i in l1+l2:
        if i not in l1 or i not in l2:
            new_lst.append(i)
    return new_lst

s=differ_lst(lst1)
print(s)