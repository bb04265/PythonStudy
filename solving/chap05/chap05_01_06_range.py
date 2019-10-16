import random
pch = 'abcdefghijklmnopqrstuvwxyz0123456789'
for x in range(3):
    password = ''
    for y in range(1, 7):
        indexNum = random.randrange(len(pch))
        password += pch[indexNum]
    print(password)