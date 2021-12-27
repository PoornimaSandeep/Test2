class add_dict:
      def __init__(self):
          print("Combine two dictionary adding values for common keys.")
          self.d1={'l':66,'o':90,'k':1,'m':1,'b':60}
          self.d2 = {'a': 1,  'l': 90, 'c': 300, "b": 40}

      def add(self):
          new_dict={}
          new_dict.update(self.d2)
          new_dict.update(self.d1)
          for i,j in self.d1.items():
              for m,n in self.d2.items():
                  if i==m:
                      new_dict[m]=(j+n)


          print(new_dict)
a=add_dict()
a.add()