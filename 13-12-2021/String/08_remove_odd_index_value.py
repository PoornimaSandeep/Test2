def rm_odd_index_value():
    print("Remove odd index values")
    str=input("please enter the string")
    words=str.split()
    d=""
    for i in words:
         for j in range(len(i)):
             if j%2==0:
                 d +=i[j]
                # print(i[j],end="")
         print(d,end=" ")
         d=""

rm_odd_index_value()
