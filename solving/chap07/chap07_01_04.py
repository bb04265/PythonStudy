def process(w):
    output = ""
    for ch in w:
        if(ch.isalpha()):
            output += ch
    return output.lower()

def count(words):
    count_dict = {}
    for each in words:
        if each in count_dict:
            count_dict[each] += 1
        else :
            count_dict[each] = 1
    return count_dict

words = []

fname = input("파일 이름 입력 : ")
file = open(fname, "r")

for line in file:
    lineWords = line.split()
    for word in lineWords:
        words.append(process(word))
        result = count(words)
print(result)




