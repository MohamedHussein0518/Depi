class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a: int, b: int) -> int:
        self.result = a + b
        return self.result

    def subtract(self, a: int, b: int) -> int:
        self.result = a - b
        return self.result

    def multiply(self, a: int, b: int) -> int:
        self.result = a * b
        return self.result

    def divide(self, a: int, b: int) -> float:
        self.result = a / b
        return self.result