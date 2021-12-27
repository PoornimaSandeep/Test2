def index_of_str(str):
    print("nth index character from string")
    print(" ")
    index=int(input("please enter index of character you want to get: "))
    for i in range(len(str)):
        if i==index:
            print("the character corresponding to this index: ",i, str[i])

str=input("enter string")
index_of_str(str)
