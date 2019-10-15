total = 0
s_list = list()
high_score = 0
while(True):
    score = int(input("성적을 입력하시오 : "))
    if score == 0:
        break
    elif score >= 80:
        high_score += 1
    s_list.append(score)
for n in range(len(s_list)):
    total += s_list[n]
print("평균 : ", total / len(s_list))
print("80점 이상 : ", high_score)