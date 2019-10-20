class Account:
    def __init__(self):
        self.balance = 500


    def withdraw(self,money):
        self.balance -= money
        return self.balance

    def deposit(self,money):
        self.balance += money
        return self.balance

account = Account()

while True:
    money = int(input("얼마 : "))
    if money == 0:
        break
    print(account.withdraw(money))







