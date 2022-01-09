class List_typy_progrrm:

      def __init__(self,l):
          self.l=l
          self.dict={}

      def  list_type(self):
           for i in self.l:
              self.dict[i]=type(i)
              print("dictionary with type",self.dict)

obj_list=List_typy_progrrm([12,45.8,"pooornima",'p'])
obj_list.list_type()

