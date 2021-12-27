def copy_4ch():
    print("4 Copies of last 2 chars")
    str=input("Please enter string")
    words=str.split()
    for i in words:
        l = len(i) - 1
        ch1=i[l]
        ch2=i[l-1]
        print((ch2*4)+(ch1*4), end=" ")

#copy_4ch()

name="shetal"
print(id(name))
name=name.capitalize()
print(id(name))