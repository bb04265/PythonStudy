class Machine:
    def __init__(self, coffee_rest, water_rest, sugar_rest):
        self.choice = 0
        self.coffee_rest = coffee_rest
        self.water_rest = water_rest
        self.sugar_rest = sugar_rest
# Machine 클래스를 정의하고 들어가는 커피,물,설탕의 개수의 변수를 정의한다

def set_rest():

    machine = Machine(coffee_rest=10, water_rest=10, sugar_rest=10)
    return machine

# set_rest함수에 커피, 물, 설탕의 개수를 10으로 초기화한다

def select(self):
    while 1:
        choice = int(input("메뉴를 눌러주세요(1:에스프레소, 2:아메리카노, 3:설탕커피, 4:잔량보기, 5:채우기) : "))
        if choice == 1 and self.coffee_rest >= 1 and self.water_rest >= 1 :
            self.coffee_rest = self.coffee_rest - 1
            print("에스프레소 입니다")

        elif choice == 2 and self.coffee_rest >= 1 and self.water_rest >= 2:
            self.coffee_rest = self.coffee_rest - 1
            self.water_rest = self.water_rest - 2
            print("아메리카노 입니다")

        elif choice == 3 and  self.coffee_rest >= 1 and self.water_rest >= 2 and self.sugar_rest >= 1:
            self.coffee_rest = self.coffee_rest - 1
            self.water_rest = self.water_rest - 2
            self.sugar_rest = self.sugar_rest - 1
            print("설탕커피 입니다")
# while 문으로 메뉴를 계속 선택할 수 있게 해주고 적절하게 커피,물,설탕의 개수를 빼준다

        elif choice == 4:
            print(self.coffee_rest, self.water_rest, self.sugar_rest)
# 4를 입력하면 남은 커피,물,설탕의 개수가 출력되게 한다
        elif choice == 5:
            self.coffee_rest = 10
            self.water_rest = 10
            self.sugar_rest = 10
            print(self.coffee_rest, self.water_rest, self.sugar_rest)
#5를 선택하면 다시 10으로 초기화 되게 한다
        else :
            print("원료가 부족합니다")
# 원료가 다 떨어지면 원료가 부족하다는 말이 뜨게 한다
while 1:
    select(set_rest())
#반복해서 실행할 수 있게 한다