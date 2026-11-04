class Add:
    def __init__(self):
        self.a=int(input("Enter frist number"))
        self.b=int(input("Enter second number"))
    def calculate(self):
        self.c=self.a+self.b
    def show(self):
        print("Ans:",self.c)

a1=Add()
a1.calculate()
a1.show()

a2=Add()
a2.calculate()
a2.show()
