def calc(x,y):
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y

    return add, sub, mul, div

x, y = list(map(int, input().split()))
print("사칙연산의 결과는")
print(calc(x, y))