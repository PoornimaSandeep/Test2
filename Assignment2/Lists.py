class List_program:

      def __init__(self):

          self.title=" List problems "
          self.l = [23, 56, 77, 9998, 8, 789,2,100,2,100]
          print(self.l)


      def sum_element(self):
          print("")
          self.title="1.sum of elements"
          print(self.title)

          res=0
          for i in self.l:
               res +=i
          print("after sum the result is: " ,res)

      def mul_element(self):
          print("")
          self.title="2.Multiply of elements"
          print(self.title)

          res=1
          for i in self.l:
               res *=i
          print("after multiplication the result is:",res)

      def largest_num(self):
          print("")
          self.title = "3.largest number in a given list"
          print(self.title)
          print("largest number in the list",max(self.l))

      def smallest_num(self):
          print("")
          self.title = "4.smallest number in a given list"
          print(self.title)
          print("Smallest number in the list ",min(self.l))

      def remove_duplicates(self):
          print("")
          self.title = "5.remove duplicates from  a given list"
          print(self.title)
          l2=set(self.l)
          print(list(l2))

      def list_empty_not(self):
          print("")
          self.title="6.check list is empty or not"
          print(self.title)
          if len(self.l)==0:
              print("list is empty")
          else:
              print("list is not empty",self.l)

      def lict_copy(self):
          print("")
          self.title = "7.copied list from another list"
          print(self.title)
          l2=[]
          for i in self.l:
              l2.append(i)
          print(l2)

      def common_ele(self):
          print("")
          self.title="8.Find common element from 2 lists"
          print(self.title)
          l2=[2,100,400,500,700]
          res=[]

          for i in self.l:
              for j in l2:
                  if i==j:
                     res.append(i)
          print("comman element from 2 list :",res)

      def remove_specific_index(self):
           print("")
           self.title="9.Remove even elements and print list"
           print(self.title)
           index=int(input("plese enter the index of element which one you want to remove"))
           res=[]
           for i in range(len(self.l)):
               if i==index:
                   continue
               else:
                   res.append(self.l[i])
           print(res)


      def remove_even(self):
           print("")
           self.title="10.Remove even elements and print list"
           print(self.title)
           res=[]
           for i in self.l:
               if i%2==0:
                   continue
               else:
                   res.append(i)
           print(res)



list_obj=List_program()
list_obj.sum_element()
list_obj.mul_element()
list_obj.largest_num()
list_obj.smallest_num()
list_obj.remove_duplicates()
list_obj.list_empty_not()
list_obj.lict_copy()
list_obj.common_ele()
list_obj.remove_specific_index()
list_obj.remove_even()

