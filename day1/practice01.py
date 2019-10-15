name = input("이름을 입력하시오 : ")
age = int(input("나이를 입력하시오 : "))
# str형으로 받아져서 year 변수에 숫자 연산을 하기 위해서 int형으로 바꿔줌
year = int(2019 + (100-age))
# 100살까지 남은 나이를 빼주고 2019에 더해줌
print(name, "님은 ", year, "년에 백살이시네요!")