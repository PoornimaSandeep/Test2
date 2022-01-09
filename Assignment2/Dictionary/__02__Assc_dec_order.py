class asc_dec_problem:
      sorted_dict = {}
      def __init__(self):
          self.title="To sort (ascending and descending) a dictionary by value"
          self.dict={'a':100,'b':20,'c':3,'d':90,'e':87}


      def asecding_ord(self):
          sorted_values = sorted(self.dict.values())  # Sort the values
          for i in sorted_values:
              for k in self.dict.keys():
                  if self.dict[k] == i:
                      asc_dec_problem.sorted_dict[k] = self.dict[k]
                      break
          print("Assending  order",asc_dec_problem.sorted_dict)

      def descending_ord(self):
          value_key_pair= ( (value,key)for (key,value) in self.dict.items())
          sorted_value_key_pairs = sorted(value_key_pair, reverse=True)
          desc_ordr={k: v for v, k in sorted_value_key_pairs}
          print("Descending order",desc_ordr)







asc=asc_dec_problem()
asc.asecding_ord()
asc.descending_ord()