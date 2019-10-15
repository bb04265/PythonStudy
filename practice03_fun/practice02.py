# random.choice함수를 사용해서 6자리의 무작위 비밀번호 생성하는 프로그램

import random

pch = "abcdefghijklmnopqrstuvwxyz0123456789"

def generatePassword():
    password = ""

    for i in range(6):
        pw = random.choice(pch)
        password += pw
    return password
# for문을 사용하여 6번 반복할 수 있게 하고 random.choice함수를 이용해서 pch문자열에서 랜덤으로 추출하여 붙여준다

print(generatePassword())
print(generatePassword())
print(generatePassword())
