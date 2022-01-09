class mul_of_dict:
    def __init__(self):
        self.d1 = {'a': 1, 'b': 100, 'c': 90, 'd': 300}

    def mul(self):
        Total = 1
        for i in self.d1.values():
            Total *= i

        print("Multiply of value", Total)


sm_obj = mul_of_dict()
sm_obj.mul()