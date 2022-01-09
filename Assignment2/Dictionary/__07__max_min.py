class max_dict:

    def __init__(self):
        print("Get the maximum and minimum value in a dictionary.")
        self.dict={'a':1,'b':100,'c':90,'d':300}

    def maximum_dict(self):
        print("maximum number",max(self.dict.values()))
    def min_dict(self):
        print("minimum value",min(self.dict.values()))

mx_dict=max_dict()
mx_dict.maximum_dict()
mx_dict.min_dict()

