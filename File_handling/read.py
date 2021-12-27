file=open("textfile/a.txt", 'r')

for i in file:
    print(i)


#using with function

with open("textfile/append.txt") as f:
      d=f.read()
      print(d)

