class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def branch(self):
        if self.a > 0:
            return 'up'
        return 'down'

    def x_sect(self):
        if self.b ** 2 - 4 * self.a * self.c > 0:
            return 2
        elif self.b ** 2 - 4 * self.a * self.c < 0:
            return 0
        return 1

    def sections(self):
        if Quadratic.x_sect(self) == 2:
            x_1 = (-self.b + (self.b ** 2 - 4 * self.a * self.c) ** 0.5) / (2 * self.a)
            x_2 = (-self.b - (self.b ** 2 - 4 * self.a * self.c) ** 0.5) / (2 * self.a)
            x_1, x_2 = sorted((x_1, x_2))
            return x_1, 0.0, x_2, 0.0
        elif Quadratic.x_sect(self) == 1:
            return -self.b / (2 * self.a), 0.0

    def top(self):
        x = -self.b / (2 * self.a)
        y = self.a * x ** 2 + self.b * x + self.c
        return x, y

    def y_sect(self):
        return 0, self.c


equation = Quadratic(1.6, 0, -3)
print(equation.branch())
print(equation.sections())
print(equation.x_sect())
print(equation.y_sect())
