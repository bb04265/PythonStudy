#사용자에게 정수를 입력받아 최대값, 최소값을 출력하는 프로그램

#s_list 를 선언한다
s_list = list()
n = 0

# 5개의 정수를 입력받아 s_list 리스트에 저장될수 있게 한다. 
for i in range(5):
    n+=1
    numbers = int(input("%d번째 숫자 : "%n))
    s_list.append(numbers)

#max함수와 min함수를 이용해서 최대값, 최소값을 구한다
print("최대값 : ", max(s_list))
print("최소값 : ", min(s_list))