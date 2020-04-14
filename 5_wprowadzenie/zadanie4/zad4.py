class Point:
    counter = []

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)

p1 = Point(0,0)
p2 = Point(1,1)
p3 = Point(1,2)
p4 = Point(2,3)
p5 = Point(2,3)

print(p1.counter)
print(p2.counter)
p1.update(1)
print(p1.counter)
p2.update(1)
print(p2.counter)
p3.update(2)
print(p3.counter)
p4.update(22)
print(p4.counter)
p5.update(23)
print(p5.counter)