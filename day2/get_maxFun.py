def get_max(num1, num2):
    if num1 > num2:
        return "첫번째 수가 더 큼"
    elif num1 < num2:
        return "두번째 수가 더 큼"
    else :
        return "두 수가 같음"

print(get_max(10,10))