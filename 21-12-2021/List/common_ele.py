print("common element from 2 lists")
l1=[1,2,3,4,5,7,89]
l2=[3,4,5,90,6,7,89]

for i in l1:
    for j in l2:
        if i in l2:
            print(i,end=",")
            break