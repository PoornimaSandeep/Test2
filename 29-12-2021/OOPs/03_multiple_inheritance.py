print("Multiple inheritance")
class Father():
    def father(self):
        print("My father name is Narayan")

class mother():
    def mother(self):
        print("My mother name is Kaveri")

class son(mother,Father):
    def son(self):
        print("My name is Sandeep")
s=son()
s.son()
s.father()
s.mother()

