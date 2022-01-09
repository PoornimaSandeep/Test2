

class check_duplicate:
      def __init__(self):
          print("Check multiple keys exists in a dictionary.")

      def duplicate_key(self):
          data = {'l': [6,9], 'o': 90, 'l': 8, 'l': 6, 'k': 1, 'm': 1}

          l=[]
          for i,j in data.items():
              if i not in l:
                  l.append(i)
              elif i in l:
                   print(i,"is a duplicate value")


cd=check_duplicate()
cd.duplicate_key()