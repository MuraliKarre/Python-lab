class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print("DRAW")
    
    def move(self):
        print("MOVE")

#point1 = Point()
#point1.move()

#point2 = Point()
#point2.draw()


point = Point(10, 20)
print(point.x)
point.y = 33
print(point.y)