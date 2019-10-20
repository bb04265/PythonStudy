class Car:

    def __init__(self, change, accelerate, slowdown):
        self.change = change
        self.accelerate = accelerate
        self.slowdown = slowdown

    def __str__(self):
        return "변속 : %d, 가속 : %d, 감속 : %d 입니다"%(self.change, self.accelerate, self.slowdown)

car1 = Car(10, 50, 30)
print(car1)