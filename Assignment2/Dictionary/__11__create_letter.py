
class letter_dict:

      def __init__(self):
          print("Create and display all combinations of letters, selecting each letter from a different key in a dictionary")
          self.d={}
      def create_dict(self):
          d={1:['a','b','c','d'],2:['e','f','g','h']}
          l=[]
          for x in d[1]:
              for y in d[2]:
                  l.append(x+y)
          print(l)

ld=letter_dict()
ld.create_dict()




