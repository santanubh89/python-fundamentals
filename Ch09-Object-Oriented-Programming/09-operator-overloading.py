class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'Vector ({self.x}i + {self.y}j + {self.z}k)'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y, self.z * other.z)


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print(f'Vector 1: {v1}')

vector_sum = v1 + v2
print(f'Vector sum: {vector_sum}')

vector_sub = v2 - v1
print(f'Vector sub: {vector_sub}')

vector_mul = v1 * v2
print(f'Vector mul: {vector_mul}')