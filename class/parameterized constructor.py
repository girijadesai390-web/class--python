class Add:
    def __init__(self,a,b):
         self.a=a 
         self.b=b 
    def calculate(self):
         self.c = self.a + self.b
    def show(self):
         print("Ans:",self.c)

a1=Add(90,10)
a1.calculate()
a1.show()

a2=Add(20,20)
a2.calculate()
a2.show()
