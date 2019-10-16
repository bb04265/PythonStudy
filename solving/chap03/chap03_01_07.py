num = int(input("이수한 학점 : "))
grade = float(input("평점 : "))

if num >= 140 and grade >= 2.0:
    print("졸업이 가능합니다")
else :
    print("졸업이 어렵습니다!")