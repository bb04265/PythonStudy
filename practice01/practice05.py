firstNum = int(input("첫번째 양의 정수 입력 : "))
secondNum = int(input("두번째 양의 정수 입력 : "))
thirdNum = int(input("세번째 양의 정수 입력 : "))

if firstNum > secondNum and firstNum >= thirdNum :
    print("제일 큰 정수는 ", firstNum, "입니다.")

elif secondNum >= thirdNum and secondNum >= firstNum :
    print("제일 큰 정수는 ", secondNum, "입니다.")

else :
    print("제일 큰 정수는 ", thirdNum, "입니다.")
