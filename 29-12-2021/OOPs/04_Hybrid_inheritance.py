print("Hybrid Inheritance")

print(" ")
class Grandfather:
    def __init__(self):
        pass
    def grandfather(self):
        print("My Grandfather name is Rangappa")


class Father(Grandfather):
    def father(self):
        print("My Grandfather name is Narayan")

class son(Father):
    def son(self):
        print("My  name is sandeep")
class daughter(Father):
    def daughter(self):
        print("My name is poornima")

s=son()
s.grandfather()
s.father()
s.son()
print("")
d=daughter()
d.grandfather()
d.father()
d.daughter()