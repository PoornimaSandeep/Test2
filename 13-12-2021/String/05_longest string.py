def long_str(str2):
    print("Length of longest string in python")
    #str2=input("please enter the string")
    st=str2.split()
    res=max(st,key=len)
    print(res)

str2=input("please enter the string")
long_str(str2)
