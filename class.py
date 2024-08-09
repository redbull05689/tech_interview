class Point():

    def __init__(self, x, y):
        # print("вызов инит")
        self.x = x
        self.y = y

    def __del__(self):
        print("удаление экхемпляра" + str(self))

pt = Point(1,3)

print(pt.__dict__)