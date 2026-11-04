class Area:
    def get_data(self,r):
        self.r=r
    def calculated (self):
        self.a=3.14*self.r*self.r 
    def show(self):
        print("Area:",self.a)       

a1=Area()
a1.get_data(12)
a1.calculated()
a1.show()     

a2=Area()
a2.get_data(18)
a2.calculated()
a2.show()