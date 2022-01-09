class Exc_handling:
      def __init__(self):
          print("Count the elements in a list until an element is a tuple")

      def search_tuple(self):
          l=[1,2,3,4,5,6,(3,4,5)]
          count=0
          for i in l:
              count +=1
              if i is tuple:
                  break;
          print("Tuple occurs at ",count,"position")

ex=Exc_handling()
ex.search_tuple()
