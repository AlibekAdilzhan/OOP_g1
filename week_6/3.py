class Calculator:
    def add(self, a, b):        
        return a + b

    def mul(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b


calc = Calculator()
assert calc.add(1, 3) == 4, "should be 4"