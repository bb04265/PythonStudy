scores = []
highGrade = 0
total = 0

for i in range(5):
    scores.append(int(input("성적을 입력하시요 : ")))
    if scores[i] >= 80 :
        highGrade += 1
    total += scores[i]

avg = total / 5

print("성적 평균은 %s 입니다"% avg)
print("80점 이상 성적을 받은 학생은 %s 입니다"%highGrade)

