import lab1 as c

class FooCalculator:

    def __init__(self):
        pass

    def sum(self, m,n):
        return c.sum(m,n)

    def divide(self,m,n):
        return c.divide(m,n)


calcolatrice = FooCalculator

print(calcolatrice.divide(calcolatrice, 13,6))

print(calcolatrice.sum(calcolatrice, 13,6))

print(calcolatrice.sum(calcolatrice, 13, -6))