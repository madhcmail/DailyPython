class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def sqSum(self):
        return (self.x * self.x + self.y * self.y + self.x * self.z)

point_1 = Point(1, 3, 5)
print(" Sum of squares= ", point_1.sqSum())