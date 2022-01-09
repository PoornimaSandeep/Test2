class swapchar:
      def __init__(self):
          print("Swapping chars in string")

      def swap_char(self,str):
          st=list(str)
          st2=list()
          temp = st[0]
          str2=""
          for i in range(1,len(st),1):
              if i%2 !=0:
                  str2 += st[i]
                  str2 += temp
              temp=st[i]

          print(str2)


sc=swapchar()
st=input("enter the string")
sc.swap_char(st)

