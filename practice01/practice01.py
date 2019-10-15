num = int(input("입력 : "))
# 정수형으로 바꿔서 숫자를 입력받는다.

if num < 0 :
    print("입력한 값은 0보다 작습니다.")
elif num >= 0 and num < 10 :
    print("입력한 값은 0이상 10미만입니다. ")
elif num >= 10 and num < 20:
    print("입력한 값은 10이상 20미만입니다.")
elif num >= 20 and num <30 :
    print("입력한 값은 20이상 30미만입니다.")

else :
    pass

# elif 문을 사용해서 나누고 30이상인 수를 입력하면 아무일도 일어나지 않는다.