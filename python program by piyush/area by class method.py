'''class Rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w= w
    def area(self):
        return self.l*self.w
l = int(input('enter the length:'))
w = int(input('enter yhe width: '))
rect = Rectangle(l,w)
print('area or rectangle is:',rect.area())'''
class Circle:
    _pi = 3.14
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print(3.14*radius*radius)
    def perameter(self):
        print(2*3.14*radius)

radius= int(input('enter the radiius:'))
c = Circle(radius)
c.area()
c.perameter()