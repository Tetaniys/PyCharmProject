class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mul(self):
        return self.x * self.y

    @staticmethod

    def mul_any(x, y):
        return x**y


a = A(10, 15)
print(a.mul())
print(a.mul_any(10, 15))
