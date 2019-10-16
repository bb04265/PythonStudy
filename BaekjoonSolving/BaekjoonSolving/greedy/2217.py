rope_num = int(input())
rope_list = []
answer = 0

for _ in range(rope_num):
    rope_list.append(int(input()))
rope_list.sort(reverse=True)

for i in range(rope_num):
    if answer < rope_list[i] * (i + 1):
        answer = rope_list[i] * (i + 1)
        
print(answer)