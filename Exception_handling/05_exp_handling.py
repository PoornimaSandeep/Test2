class Exp_handling5:
      def __init__(self):
          print("reverse a string")

      def reverse_str(self):
          try:
              str = input("enter the string")
              print(str[::-1])
              print(k)
          except Exception as e:
               print("Exception:",e)



exp5=Exp_handling5()
exp5.reverse_str()