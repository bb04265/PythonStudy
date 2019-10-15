firstNum = int(input("첫번째 숫자를 입력하시오 : "))
secondNum = int(input("두번째 숫자를 입력하시오 : "))
thirdNum = int(input("세번쨰 숫자를 입력하시오 : "))
# 숫자들을 int형으로 바꾼다

avg = int((firstNum + secondNum + thirdNum)/3 )
# 들어온 숫자들을 다 더해서 3으로 나눠준다

print(firstNum, secondNum, thirdNum, "의 평균은 ", avg)