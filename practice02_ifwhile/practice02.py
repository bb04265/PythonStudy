# for문과 while문의 중첩을 사용하여 별을 순서대로 출력하는 프로그램

while True:
    for x in range(5):
        x += 1
        print("*"*x)
    break

# while의 무한루프를 사용해서 변수 x에 0~4까지의 숫자를 넣어서 1개씩 늘어나게 해서 별을 출력하게 하고 숫자범위에서 벗어나면 break시킨다