#lab 9-9

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def size(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def __gt__(self, other):
        return self.size() > other.size()

    def __ge__(self, other):
        return self.size() >= other.size()

    def __lt__(self, other):
        return self.size() < other.size()

    def __le__(self, other):
        return self.size() <= other.size()


v1 = Vector2D(30, 40)
v2 = Vector2D(10, 20)

print('v1 > v2 =', v1 > v2)
print('v1 >= v2 =', v1 >= v2)
print('v1 < v2 =', v1 < v2)
print('v1 <= v2 =', v1 <= v2)
