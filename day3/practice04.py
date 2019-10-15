#단어의 빈도수를 세는 프로그램

# 단어에서 구두점을 제거하고 소문자로 만든다.
def process(w):
    output = ""
    for ch in w:
        if( ch.isalpha()):
            output += ch
    return output.lower()

#단어와 단어의 수를 저장할 word_count라는 딕셔너리를 만든다
words = set()
word_count = {}
#파일을 연다
fname = input("입력 파일 이름: ")
file = open(fname, "r")

#파일의 모든 줄에 대하여 반복한다.
for line in file:
    lineWords = line.split()        #단어를 구분하여 리스트로 저장
    for word in lineWords:
        words.add(process(word))

#word_count에 단어가 나올때마다 1을 추가해주고 아니라면 1개로 저장한다
    for each in words:
        if each in word_count:
                word_count[each] += 1
        else:
                word_count[each] = 1
#출력한다
    for key in word_count:
        print (key, ':' ,word_count[key])
