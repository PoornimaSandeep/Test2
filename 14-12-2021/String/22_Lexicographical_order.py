print("program to sort a string lexicographically")
str = input("enter the string")

print(" ")
print("1.using built is function")
words = str.split()
words.sort()
print(words)

print(" ")
print("2.Using algorithm")
print("step1 :split string into words")
list1 = []
st = ""
l = len(str)
for i in range(l):

    if str[i] == ' ' or i == l - 1:
        list1.append(st)
        st = ""
    else:
        st += str[i]
print("step2:sort an elements in lexicograpicall manner")
list2 = []
for i in list1:
    if i[0].isdigit():
        list2.append(i)
for i in list1:
    if  i[0].isupper():
        list2.append(i)
for i in list1:
    if i[0].islower():
        list2.append(i)

print(list2)


print("")
print("3.Using userdefined function")
def lexigrph(str):
    list1 = []
    st = ""
    l = len(str)
    for i in range(l):

        if str[i] == ' ' or i == l - 1:
            list1.append(st)
            st = ""
        else:
            st += str[i]
    #print("step2:sort an elements in lexicograpicall manner")
    list2 = []
    for i in list1:
        if i[0].isdigit():
            list2.append(i)
    for i in list1:
        if i[0].isupper():
            list2.append(i)
    for i in list1:
        if i[0].islower():
            list2.append(i)

    print(list2)
lexigrph(str)

