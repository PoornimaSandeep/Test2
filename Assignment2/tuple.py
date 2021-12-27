class tuple_problems:
      def __init__(self):
          self.title="tuple problems"
          self.t=(100,90,89,(12,34,56))

      def create_tuple(self):
          print("")
          self.title="1.create tuple"
          print(self.title)
          print(self.t)

      def tuple_diff_datatype(self):
          print(" ")
          self.title=("2.create a tuple with different data types")
          print(self.title)
          tu_pl=(100,"qoiiror",90.0,"233@#")
          print("different data type",tu_pl)

      def tuple_num(self):
          print("")
          self.title=("3.create a tuple with numbers and print one item")
          print(self.title)
          t_num=(23,45,67,89,99)
          print("tuple:",t_num)
          print("one element from tuple: ",t_num[3])

      def tuple_unpack(self):
          print(" ")
          self.title=("4.unpack a tuple in several variables")
          print(self.title)
          a=("poornima",25,9739935941)
          b=("Sandeep",30,9686252049)
         # (name,age,mobile_no)=a
          (name,age,mobile_no)=b
          print(f"name: {name} , age:{age} , mobile_no:{mobile_no}")

      def tuple_additem(self):
          print(" ")
          self.title="5.add an item in a tuple."
          print(self.title)
          l=list(self.t)
          l.append(1000)
          print(tuple(l))

      def tuple_convertstr(self):
          print(" ")
          self.title="6.convert a tuple to a string"
          print(self.title)
          tuple=('p','o','o','r','n','i','m','a')
          str=" "
          for i in tuple:
              str +=i
          print(str)





obj_tuple=tuple_problems()
obj_tuple.create_tuple()
obj_tuple.tuple_diff_datatype()
obj_tuple.tuple_num()
obj_tuple.tuple_unpack()
obj_tuple.tuple_additem()
obj_tuple.tuple_convertstr()