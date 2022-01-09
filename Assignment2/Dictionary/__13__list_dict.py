from collections import Counter
class list_of_dict:

      def __init__(self):
          print("Combine values in python list of dictionaries.")

      def merge_dict(self):
         l=[{'item':'pen','amount':100},{'item':'book','amount':100},{'item':'pen','amount':100}]

         result = Counter()
         for d in l:
             result[d['item']] += d['amount']
         print(result)
ld=list_of_dict()
ld.merge_dict()


