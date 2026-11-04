class Add:
    def get_data(self,a,b):
        self.a=a 
        self.b=b 
    def calculate (self):
        self.c=self.a + self.b 
    def show (self):  
        print("Answer:",self.c)  

a1=Add()
a1.get_data(10,20)
a1.calculate()
a1.show()

a2=Add()
a2.get_data(40,10)
a2.calculate()
a2.show()