class Simple:
       def __init__(self):
              self.p = int(input("Enter the number"))
              self.r = int(input("Enter the number"))
              self.t = int(input("Enter the number"))
       def calculate(self):
              self.si = self.p*self.r*self.t/100 
       def show(self):
              print("Ans:",self.si)         

a1=Simple()
a1.calculate()
a1.show()

