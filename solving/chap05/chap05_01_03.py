def power():
    result = 0
    result = num[0]**num[1]
    return result

num = list(map(int, input().split()))
print(power())