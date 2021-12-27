class opr_dict:
      def __init__(self):
          print("To get the key, value and item in a dictionary. ")

      def opr(self):
          data = {'l': [6, 9], 'o': 90, 'l': 8, 'l': 6, 'k': 1, 'm': 1}
          print(data.values())
          print(data.keys())
          print(data.items())

op=opr_dict()
op.opr()