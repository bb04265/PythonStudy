# 성적을 비율에 맞게 합산하는 프로그램

#n차를 나타내기 위한 변수 선언과 s_list선언
n = 0
s_list = list()

#정수를 4번 입력받아서 리스트에 저장해준다
for i in range(4):
    n+=1
    grades = int(input("%d차 시험 : "%n))
    s_list.append(grades)

#리스트의 인덱스를 이용해서 비중에 따라 합산할 수 있게 한다.
total = (s_list[0]*0.1)+(s_list[1]*0.2)+(s_list[2]*0.3)+(s_list[3]*0.4)
print("합계 : ", total)