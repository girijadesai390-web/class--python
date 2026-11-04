class Area:
      def __init__(self):
            self.l=int(input("Enter the number"))
            self.b=int(input("Enter the number"))
      def calculate(self):
            self.a = self.l*self.b
      def show(self):
            print("Ans:",self.a) 

a1=Area()
a1.calculate()
a1.show()                      