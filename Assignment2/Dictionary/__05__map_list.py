class map_list:
      def __init__(self):
          print("Map two lists into a dictionary")

      def m_list(self):
          key=["p","l","o","y"]
          value = [12, 34, 56, 78, 90]
          d={}
          res = {key[i]: value[i] for i in range(len(key))}
          print(res)

mp=map_list()
mp.m_list()
