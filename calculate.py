class ComplexCalculator:
    def __init__(self, operation):
        self.operation = operation

    def calculate(self, num1, num2):
        return self.operation.operate(num1, num2)

    def __str__(self):
        return str(self.operation)