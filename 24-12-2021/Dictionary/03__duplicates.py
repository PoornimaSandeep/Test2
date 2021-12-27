class remove_duplicates:

      def __init__(self):
          print("Remove duplicates from Dictionary")
          self.data={'l':6,'o':90,'l':8,'l':6,'k':1,'m':1}
          print(self.data)

      def remove(self):
         new_dict={}
         for i,j in self.data.items():
               if i not in new_dict.keys():
                     if j not in new_dict.values():
                         new_dict[i]=j
         print("remove duplicate key",new_dict)


rm_dp=remove_duplicates()
rm_dp.remove()
