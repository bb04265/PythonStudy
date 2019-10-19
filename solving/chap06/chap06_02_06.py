total = 0
count = 1
grades = []
for i in range(4):
    grade = int(input("%d차 시험 : "%count))
    grades.append(grade)
    count += 1

total = grades[0]*0.1 + grades[1]* 0.2 + grades[2]*0.3 + grades[3]*0.4
print(total)