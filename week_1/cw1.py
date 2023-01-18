class MyCar:
    def __init__(self, name, color="black"):
        self.__a = "5"
        self.car_name = name        
        self.engine = "petrol"
        self.s = 0

    def go_straight(self, a):
        self.s = self.s + a
        print("going straing", self.s)


c1 = MyCar("BMW", "black")
c1.go_straight(8)
c1.go_straight(19)
c1.__a