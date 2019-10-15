# random.randrange함수를 사용해서 6자리의 무작위 비밀번호 생성하는 프로그램

import random

pch = "abcdefghijklmnopqrstuvwxyz0123456789"

def generatePassword():
    password = ""

    for i in range(6):
# 6자리 비밀번호를 생성할 수 있도록 for문 사용
        num = random.randrange(1, 36)
# pch 문자열에서 n자리 수의 자리에 해당하는 문자나 숫자를 뽑아내기 위함
        password += pch[num]
# pch 문자열에서 무작위 추출한 문자나 숫자를 붙여준다
    return password

print(generatePassword())
print(generatePassword())
print(generatePassword())