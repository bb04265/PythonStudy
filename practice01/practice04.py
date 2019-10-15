applePrice = 1000
grapePrice = 3000
pearsPrice = 2000
mandarinePrice = 500
# 과일들의 가격을 지정해줌

apple = int(input("구매한 사과의 개수 : "))
grape = int(input("구매한 포도의 개수 : "))
pears = int(input("구매한 배의 개수 : "))
mandarine = int(input("구매한 귤의 개수 : "))
# 과일들의 구매 개수를 정수형으로 입력받는다.

total = (applePrice * apple) + (grapePrice * grape) + (pearsPrice * pears) + (mandarinePrice * mandarine)
# 개수와 금액을 곱하고 모두 더한 총 결제금액

if grape >= 3 :
    print("결제할 금액은 ", total - (total * 0.1), "입니다. ")

else :
    print("결제할 금액은" , total, "입니다. ")

# 포도 구매개수가 3개 이상일 때 10퍼센트를 할인한 금액이 나오게 하고 아니라면 그냥 총 결제금액이 나오게 하였다.