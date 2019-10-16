def get_max():
    if num[0] > num[1]:
        return num[0]
    elif num[0] < num[1]:
        return num[1]
    else :
        return "두 수는 같음"

num = list(map(int, input().split()))
print(get_max())