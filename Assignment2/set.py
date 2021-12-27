class set_problems:

    def __init__(self):
        self.title=" set problems"
        self.set={1,23,456,78,89}

    def set_additem(self):
        print("")
        self.title="1.add item into set"
        print(self.title)
        self.set.add(1000)
        print(self.set)

    def set_removeitem(self):
        print("")
        self.title="2.Remove item(s) from set "
        print(self.title)
        self.set.remove(23)
        print(self.set)

    def set_remove_item2(self):
        print("")
        self.title="3.search and remove element"
        print(self.title)
        key="45"
        if key in self.set:
            self.set.remove(key)
        else:
            print("key is not present in set")

    def set_intersection(self):
        print("")
        self.title="Create an intersection of sets"
        print(self.title)
        s1={1,2,3,4,5,9 ,7}
        s2={6,7,8,9}
        print(s1.intersection(s2))

    def set_union(self):
        print(" ")
        self.title="Create a union of sets"
        print(self.title)
        s3={'a','b','c','d'}
        s4={'e','f','g','h'}
        print(s3.union(s4))





set_obj=set_problems()
set_obj.set_additem()
set_obj.set_removeitem()
set_obj.set_remove_item2()
set_obj.set_intersection()
set_obj.set_union()