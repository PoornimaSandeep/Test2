print("polymorphism")
print("polymorphism means the same function name (but different signatures) being used for different types. this will also called method "
      "overiding")
print("multilevel inheritance")
class Grandfather:
    def __init__(self):
        pass
    def grandfather(self):
        print("My Grandfather name is Rangappa")

class maternal(Grandfather):
      def grandfather(self):
          print("My maternal grandfather name is devaraju")
class Paternal(Grandfather):
      def grandfather(self):
          print("My paternal grandfather name is Kamanna")

m=maternal()
m.grandfather()
p=Paternal()
p.grandfather()