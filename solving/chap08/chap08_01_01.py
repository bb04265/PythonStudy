class Circle:
    def __init__(self):
        self.result = 0

    def area(self, radius):
        result = radius * radius * 3.14
        return result

    def round(self, radius):
        result = 2 * radius * 3.14
        return result
circle = Circle()
while True:
    radius = int(input("원의 반지름 : "))
    if radius == 0:
        break
    print("원의 넓이 : ", circle.area(radius))
    print("원의 둘레 : ", circle.round(radius))