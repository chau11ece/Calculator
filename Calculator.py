class Calculator:
    def __init__(self, num1, sign, num2, result=0):
        self.num1 = num1
        self.sign = sign
        self.num2 = num2
        self.result = result

    def plus(self):
        return self.num1 + self.num2

    def minus(self):
        return self.num1 - self.num2

    def multiplex(self):
        return self.num1 * self.num2

    def div(self):
        if self.num1 == 0 or self.num2 == 0:
            print("Sorry cannot divide by 0. Pls enter another number!")
        else:
            return self.num1 / self.num2

    def percentage(self):
        return self.num1 % self.num2

    def __str__(self):

        if self.sign == "+":
            self.result = self.plus()
            return f"The calculation {self.num1} {self.sign} {self.num2}. \nOutput: {self.result}"

        elif self.sign == "-":
            self.result = self.minus()
            return f"The calculation {self.num1} {self.sign} {self.num2}. \nOutput: {self.result}"

        elif self.sign == "*":
            self.result = self.multiplex()
            return f"The calculation {self.num1} {self.sign} {self.num2}. \nOutput: {self.result}"

        elif self.sign == "/":
            self.result = self.div()
            return f"The calculation {self.num1} {self.sign} {self.num2}. \nOutput: {self.result}"

        elif self.sign == "%":
            self.result = self.percentage()
            return f"The calculation {self.num1} {self.sign} {self.num2}. \nOutput: {self.result}"

        else:
            print("Something went wrong. Try again!")


c1 = Calculator(46, "*", 2)
print(c1)

#print(f"{c1.num1}\n {c1.sign}\n {c1.num2}\n {c1.result}")



