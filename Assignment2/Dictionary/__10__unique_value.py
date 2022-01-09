class unique_dict:

    def __init__(self):
        print("Print all unique values in a dictionary. ")
        self.d1 = {'a': 1, 'l': 90, 'c': 300, "b": 40,'k':100,'m':100,'h':1}

    def get_unique(self):
        l=[]
        for i in self.d1.values():
            if i not in l:
                l.append(i)
        print("unique value",l)

und=unique_dict()
print(und.d1)
und.get_unique()