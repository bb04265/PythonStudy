print("현재 소지하고 있는 금액 : ", end="\n")
myMoney = int(input())
print("구매하려는 물건의 가격 : ", end="\n")
candyPrice = int(input())
numCandies = myMoney // candyPrice
change = myMoney % candyPrice

print("물건의 최대 구매 가능 개수", numCandies)
print("구입하고 남은 금액", change)

