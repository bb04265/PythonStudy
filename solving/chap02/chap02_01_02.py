myMoney = int(input("돈 : "))
candyPrice = int(input("사탕 가격 : "))
numCandies = myMoney//candyPrice
change = myMoney-(numCandies*candyPrice)

print(numCandies, change)