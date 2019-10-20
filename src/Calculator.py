def addition(a, b):
    c = a + b
    return c


def subtraction(a, b):
    c = a - b
    return c


def multiplication(a, b):
    c = a * b
    return c


def division(a, b):
    c = a / b
    return c


def square(a, b):
    c = a ** b
    return c


def sqrt(a):
    c = a ** (1 / 2)
    return c


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a, b):
        self.result = square(a, b)
        return self.result

    def sqrt(self, a):
        self.result = sqrt(a)
        return self.result

    def squareroot(self, a):
        self.result = squareroot(a)
        return self.result


