from collections import Counter
class high3value:

      def __init__(self):
          print("Find the highest 3 values in a dictionary.")

      def get_high_3value(self):
          d={'a': 1, 'l': 90, 'c': 300, "b": 40,'k':100,'m':90,'h':1}
          k=Counter(d)
          high=k.most_common(3)
          print("dict: ",d)
          print("highest 3 value: ",dict(high))



h3=high3value()
h3.get_high_3value()

