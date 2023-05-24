class Var:
    a = 10
    def __init__(self,y,z):
        self.y = y
        self.z = z
    def display(self):
        print(self.a,self.y,self.z)
v1 = Var(5,15)
v2 = Var(6,10)
print(Var.a,v1.a,v2.a)
v1.display()
v2.display()
print(Var.a,v1.y,v2.z)