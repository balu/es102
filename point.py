class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def manhattan_distance(p, q):
    dx = abs(p.x - q.x)
    dy = abs(p.y - q.y)
    return dx + dy

a = Point(2, 2)
b = Point(3, 4)
print(type(a))
print(manhattan_distance(a, b))