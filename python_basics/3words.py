'''
삼행시 짓기앱

1. 삼행시를 지을 세 글자짜리 단어를 입력한다.
2. 입력한 단어에서 한 글자씩 떼서 운을 띄워준다.
3. 띄운 운에 맞는 시 한 줄을 입력한다.
4. 띄운 운과 같은 글자로 시작하는지 체크한다. ㅇ
5. 글자를 제대로 맞추었다면 다음 글자를 보여준다.
6. 세 글자 모두 완성하면 세 줄을 합쳐 출력해 보여준다. ㅇ

필요한것
 - input 명령어
 - 글자의 위치를 알 수 있는 string[n]
 - for 반복문
'''
def zzangna(word_in):
    word_poem = [] #삼행시 저장용 리스트
    words = word_in #삼행시 지을 세글자 입력
    poem = 0
    for w in words:
        while True:
            print(w) #운 띄우기
            poem = input(" => ")
            if w == poem[0]:
                word_poem.append(poem) #입력받기
                break
            else:
                print("첫 글자를 다시 확인해라")
                continue
    for i in word_poem:
        print(f"{i[0]} : {i}")

zzangna(input("삼행시 짓기위한 세 글자를 입력하세요 : "))

'''
input : 숫자를 넣어도 숫자가 문자열이 된다. int(input(:))

for i in range(10):
    print(i)

'''