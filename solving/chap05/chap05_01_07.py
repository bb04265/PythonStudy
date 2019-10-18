def add(num1, operator, num2):
    return num1+num2
def sub(num1, operator, num2):
    return num1-num2
def mul(num1, operator, num2):
    return num1 * num2
def div(num1, operator, num2):
    return num1 / num2


print(add(operator=input("연산자 :"), num1=int(input("첫번째피연산자: ")), num2=int(input("두번쨰피연산자 :"))))