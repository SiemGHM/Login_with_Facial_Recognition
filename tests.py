class Number:
    def __init__(self):
        self.num = 0

    def setNum(self, x):
        self.num = x

# na= Number()
# na.setNum(3)
# print(hasattr(na, 'id'))

a = ABCDEFGHIJKLMNOPQRSTUVWXYZ
b = BLUESKYACDFGHIJMNOPQRTVWXZ






class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def __str__(self):
        return (self.x, self.y)

    def __add__(self, p2):
        return 4


p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1+p2)
