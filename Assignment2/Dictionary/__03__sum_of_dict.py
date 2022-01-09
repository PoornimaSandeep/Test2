class sum_of_dict:
      def __init__(self):
           self.d1={'a':1,'b':100,'c':90,'d':300}

      def sum(self):
          Total=0
          for i in self.d1.values():
              Total +=i

          print("sum of value",Total)

sm_obj=sum_of_dict()
sm_obj.sum()