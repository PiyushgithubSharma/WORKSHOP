class Car:
    base_price = 100000
    def __init__(self,door,window):
        self.door = door
        self.window = window
    def what_base_price(self):
        print('the base price is',self.base_price)
    @classmethod
    def revise_base_price(cls,inflaction):
        cls.base_price = cls.base_price+cls.base_price*inflaction
car1 = Car(2,2000)
car2 = Car(3,4000)
Car.revise_base_price(0.10)
#car1.revise_base_price(0.10)
car1.what_base_price()
car1.what_base_price()
car2.what_base_price()