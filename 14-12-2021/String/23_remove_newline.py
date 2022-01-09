print("program to remove a newline in Python")

str="jndnd \n rhrrufjnf \n rrhbjrb \n"
print("before:" ,str)
words=str.split()
print("after remove newline ")
for i in words:
    if i=="\n":
        i==" "
    print(i,end=" ")