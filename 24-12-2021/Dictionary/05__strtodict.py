class str_dct:
      def __init__(self):
          print("Create a dictionary from a string. ")

      def str_to_dict(self):
          str="{'item':'book','amount':100}"
          dict=eval(str) #eval is a built in function used to convert string to dict
          print(dict)

sd=str_dct()
sd.str_to_dict()