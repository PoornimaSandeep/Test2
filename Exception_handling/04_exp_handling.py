import array as arr
class Exc_handling4:
      def __init__(self):
          print("Get the number of occurrences of a specified element in an array")

      def count_ele(self):
          try:
              d = arr.array('i', [1, 2, 4, 5, 4, 9, 4, 4])
              ele = int(input("Enter the element you are searching"))
              c = 0
              for i in d:
                  if i == ele:
                      c += 1
              print(ele, "occours at", c, "times in array")
          except Exception as e:
                print("exception :",e)


exs=Exc_handling4()
exs.count_ele()