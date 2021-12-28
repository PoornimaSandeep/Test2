import array as ar
class array1:

      def __init__(self):
          print("Create an array of 5 integers and display the array items. Access individual element through indexes.")

      def create_array(self):
           a=ar.array('i',[1,2,3,4,5])

           for i in range(len(a)):
               print(a[i],end=",")

arr=array1()
arr.create_array()