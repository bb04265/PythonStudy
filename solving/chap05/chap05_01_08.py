def CtoF():
    f = c * 1.8 + 32
    return f

def FtoC():
    c = (f - 32) / 1.8
    return c

while True:
    choice = input("메뉴를 선택하세요 : ")
    if choice == 'c':
        c = float(input("섭씨 온도 : "))
        print(CtoF())
    elif choice == 'f':
        f = float(input("화씨 온도 : "))
        print(FtoC())
    elif choice == 'q':
        print("프로그램 종료")
        break
    else :
        print("c, f, q 만 입력하세요")




