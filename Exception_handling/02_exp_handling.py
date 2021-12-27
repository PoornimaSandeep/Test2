class exp_handling2:

      def __init__(self):
          print("Create a shallow copy of sets. ")

      def shallow_cp(self):

          l=[]
          try:
              n = int(input("enter the no element you add into set"))
              if n>3:
                 for i in range(n):
                     ele = input("please enter the element")
                     l.append(ele)
                     s=set(l)
                     t=[]
                 for i in s:
                       t.append(i)
                 print(l)
                 print("original set: ",s)
                 print("shallow copy of s: ",set(t))
          except ValueError :
                  print("invalid data ",ValueError)
          except Exception as e :
                  print("error occured",e)

exp2=exp_handling2()
exp2.shallow_cp()