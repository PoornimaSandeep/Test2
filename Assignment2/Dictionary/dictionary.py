


class dict_problem:
      def __init__(self):
          self.title="Dictionary problem"
          self.dict={'name':'poornima','age':25,'mobileno':9739935941}

      def  dict_addkey(self):
          print("")
          print("1.add item into dictionary")
          self.dict.update({"address":"Banaswadi"})
          print(self.dict)

      def check_key(self):
          print("")
          print("2.check key in dictionary")
          key="age"
          if key in self.dict.keys():
              print("key is already exist")
          else:
              print("key is not present ")

      def dict_mul(self):
          print("")
          print("3.Generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)")
          mul_dict={}
          n=int(input("enter the n value :"))
          for i in range(1,n+1):
              mul_dict[i]=i*i
          print(mul_dict)

      def dict_square(self):
          print(" ")
          print("4.Print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys")
          sqr_dict = {}

          for i in range(1, 15+1):
              sqr_dict[i] = i * i
          print(sqr_dict)

      def merge_dict(self):
          print("")
          print("5.Merge two Python dictionaries")
          def Merge(dict1, dict2):
              res = dict1 | dict2
              return res

          # Driver code
          dict1 = {'x': 10, 'y': 8}
          dict2 = {'a': 6, 'b': 4}
          dict3 = Merge(dict1, dict2)
          print(dict3)


dict_obj=dict_problem()
dict_obj.dict_addkey()
dict_obj.check_key()
dict_obj.dict_mul()
dict_obj.dict_square()
dict_obj.merge_dict()
