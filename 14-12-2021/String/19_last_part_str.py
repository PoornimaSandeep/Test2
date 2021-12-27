#state
str=input("enter the string")

print("using built in function")
words=str.split()
print("last part in string :",words[-1])

print(" ")
print("using algorithm")
list1=[]
st=""
l=len(str)
for i in range(l):
    st +=str[i]
    if str[i]==' ' or i==l-1:
        list1.append(st)
        st=""
print("last part in a string: ",list1[-1])


print(" ")
print("using user defined function")
def last_part_str(str):
    list1 = []
    st = ""
    l = len(str)
    for i in range(l):
        st += str[i]
        if str[i] == ' ' or i == l - 1:
            list1.append(st)
            st = ""
    print("last part in a string :", list1[-1])

last_part_str(str)

print(" ")
print("using oops")
class last_part:
      def __init__(self):
          pass

      def last_part_str(str):
          list1 = []
          st = ""
          l = len(str)
          for i in range(l):
              st += str[i]
              if str[i] == ' ' or i == l - 1:
                  list1.append(st)
                  st = ""
          print("last part in a string :", list1[-1])

lp=last_part
lp.last_part_str(str)