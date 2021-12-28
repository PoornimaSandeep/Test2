import array as ar
class array2:
      def __init__(self):
          print("Append a new item to the end of the array.")

      def add_item(self):
          a=ar.array('i',[1,2,3,4,5])
          a.append(90)
          print(a)


arr=array2()
arr.add_item()