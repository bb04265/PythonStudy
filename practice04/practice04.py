# max와 min함수를 사용하지 않고 최대값 최소값 구하는 프로그램

#s_list 를 선언한다
s_list = list()
n = 0

# 5개의 정수를 입력받아 s_list 리스트에 저장될수 있게 한다.
for i in range(5):
    n += 1
    numbers = int(input("%d번째 숫자 : "%n))
    s_list.append(numbers)

# max함수를 만든다. s_list의 숫자들을 for문으로 i 변수에 넣어서 비교하는 방식으로 가장 큰 값을 찾는다
def max():
    length = len(s_list)
    max_result = s_list[0]
    for i in range(length):
        if max_result < s_list[i]:
            max_result = s_list[i]
    return max_result
# max함수와 같은 방식으로 최소값을 찾는 min함수를 만든다
def min():
    length = len(s_list)
    min_result = s_list[0]
    for i in range(length):
        if min_result > s_list[i]:
            min_result = s_list[i]
    return min_result

print("최대값은 ", max(), "입니다.")
print("최소값은 ", min(), "입니다.")