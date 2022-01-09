from collections import Counter
class exphandling1:

      def __init__(self):
          print("Find the highest 3 values in a dictionary.")

      def high_3value(self):
          d={}
          try:
              n = int(input("Enter the len of the dictionary"))
              for i in range(n):
                  key = input("enter the key")
                  value = int(input("enter the value"))
                  d[key] = value
              k = Counter(d)
              high = k.most_common(3)
              print("dict: ", d)
              print("highest 3 value: ", dict(high))
          except Exception as e:
                 print("exception occured",e)


exp1=exphandling1()
exp1.high_3value()