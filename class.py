class Point():
    # def __new__(cls, *args, **kwarg) : #Необязательный метод
    #     print("вызов __new__ для" + str(cls))
    #     return super().__new__(cls)


    def __init__(self, x, y):
        # print("вызов инит")
        self.x = x
        self.y = y

    # def __del__(self): #Необязательный метод
    #     print("удаление экхемпляра" + str(self))
