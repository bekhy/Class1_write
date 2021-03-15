number11 = float(input("Введите первое значение: "))
number22 = float(input("Введите второе значение: "))
operation1 = str(input("Введите операцию: "))
class Calculator:
    def __init__(self, number1, number2, operation):
        self.number1 = number1
        self.number2 = number2
        self.operation = operation

    def plus(self):
        res1 = self.number1 + self.number2
        return res1
    def minus(self):
        res2 = self.number1 - self.number2
        return res2
    def multipl(self):
        res3 = self.number1 * self.number2
        return res3
    def division(self):
        res4 = self.number1 / self.number2
        return res4

    def result(self):
        if self.operation == "+":
            res = self.plus()
            return res
        elif self.operation == "-":
            res = self.minus()
            return res
        elif self.operation == "*":
            res = self.multipl()
            return res
        else:
            res = self.division()
            return res
calc = Calculator(number11, number22, operation1)
print(calc.result())