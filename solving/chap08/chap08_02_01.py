class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def inputAge(self, age):
        self.age = age

    def introduce(self):
        print("이름은 %s이고 나이는 %d 살입니다"%(self.name, self.age))

mike = Person("Mike", 26)
mike.inputAge(28)
mike.introduce()