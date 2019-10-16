import random
i = 1

lotto = random.randint(1,100)

while True:
    num = int(input())
    if lotto < num:
        print("높음!")
        i += 1
    elif lotto > num:
        print("낮음!")
        i += 1
    else:
        print("축하합니다. 시도횟수=%d"%i)
        break