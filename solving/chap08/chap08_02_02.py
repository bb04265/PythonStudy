class CoffeeMachine:
    def __init__(self, coffee_rest, water_rest, sugar_rest):
        self.coffee_rest = coffee_rest
        self.water_rest = water_rest
        self.sugar_rest = sugar_rest

    def setRest(self):
        self.coffee_rest = 10
        self.water_rest = 10
        self.sugar_rest = 10

    def show(self):
        return "커피 : ", self.coffee_rest, "물 : ", self.water_rest, "설탕 : ", self.sugar_rest

    def manage(self):
        if select == 1 and self.coffee_rest >= 1 :
            self.coffee_rest -= 1
            print("에스프레소 입니다")
        elif select == 2 and self.coffee_rest >= 1 and self.water_rest >= 2:
            self.coffee_rest -= 1
            self.water_rest -= 2
            print("아메리카노 입니다")
        elif select == 3 and self.coffee_rest >= 1 and self.water_rest >= 2 and self.sugar_rest >= 1:
            self.coffee_rest -= 1
            self.water_rest -= 2
            self.sugar_rest -= 1
            print("설탕커피 입니다")
        elif select == 4:
            print(machine1.show())
        elif select == 5:
            machine1.setRest()
            print(machine1.show())
        else :
            print("다시 입력하세요")

machine1 = CoffeeMachine(10, 10, 10)
print("==========커피자판기가 동작합니다============")
while True:
    select = int(input("메뉴를 눌러주세요 : "))
    if select == 0:
        break
    machine1.manage()
