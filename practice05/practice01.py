class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
#Person 클래스의 멤버변수를 생성해준다

    def inputName(self, name):
        self.name = name

    def inputAge(self, age):
        self.age = age
# 이름과 나이를 입력하는 inputName, inputAge 멤버 메소드를 작성해준다

    def introduce(self):
        print(
                "이름은 ", self.name, "이고", "나이는 ", self.age, "입니다"
        )
# introduce 메소드로 이름과 나이를 출력할 수 있게 한다.
mike = Person("Mike", 26)
mike.inputAge(28)
mike.introduce()