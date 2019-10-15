# 사용자가 입력한 정수의 합계를 구하는 프로그램

#total변수와 s_list를 선언해준다
total = 0
s_list = list()
n = 0

#정수를 3번 입력받아서 s_list에 저장될 수 있게 한다
for i in range(3):
    n+=1
    numbers = int(input("%d번째 숫자 : "%n))
    s_list.append(numbers)

#합계를 구한다
for n in range(len(s_list)):
    total += s_list[n]

print("합계 : ", total)