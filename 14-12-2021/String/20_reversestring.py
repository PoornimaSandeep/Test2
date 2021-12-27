print(" reverses a string if it's length is a multiple of 4")
str=input("Enter your string")

print("1.using built in function")
words=str.split()
for i in words:
    if len(i)%4==0:
        print(i[::-1],end=" ")

print("")
print("")
print("2.Using algorithm")
list1=[]
st=""
l=len(str)
for i in range(l):
    st +=str[i]
    if str[i]==' ' or i==l-1:
        list1.append(st)
        st=""
for i in words:
    if len(i)%4==0:
        print(i[::-1],end=" ")

print("")
print("")
print("3.Using userdefined function")
def reverse_str(str):
    list1 = []
    st = ""
    l = len(str)
    for i in range(l):
        st += str[i]
        if str[i] == ' ' or i == l - 1:
            list1.append(st)
            st = ""
    for i in words:
        if len(i) % 4 == 0:
            print(i[::-1], end=" ")

reverse_str(str)

print("")
print("")
print("4.Using Oops")
class rev_str:
      def __init__(self):
          pass

      def reverse_str(str):
          list1 = []
          st = ""
          l = len(str)
          for i in range(l):
              st += str[i]
              if str[i] == ' ' or i == l - 1:
                  list1.append(st)
                  st = ""
          for i in words:
              if len(i) % 4 == 0:
                  print(i[::-1], end=" ")

rs=rev_str
rs.reverse_str(str)