'''
오늘의 앱 : 삼행시 띄워주는 앱.

세 글자를 입력하면
각각 머릿글자를 하나씩 띄워주고,
머릿글자에 맞게 시를 모두 쓰면
마지막에 아래의 형태로 출력해주는
프로그램을 작성하시오.

마지막에 화면에 표시될 내용

최 : 최홍석 왔네?
홍 : 홍석이 셤 잘 봤니?
석 : 석굴암에서 뛰어내려. 그 점수면 지옥 가능 ㅋㅋㅋ

1. 한글로 쭉 코드를 생각해서 단계를 적어보면 편함.
2. 삼행시를 지을때 제시어와 다른 글자로 시작하면 체크해서 다시 입력하라고 할것.
3. 사용되어야 할 중요 코드.
 - input()
 - for i in 리스트명: = 리스트의 0번째부터 마지막까지를 i에 넣어가며 반복
 - while ~
 - if ~ else ~ 
 - 최홍석[0] = 최
 - 리스트명.append(넣을내용)
 - print(f"{변수} 고정된 글 {변수}")

'''
# def samhaengsi():
name = ""
name3 = []
name_in = ""
name = input("삼행시 지을 세글자 넣으시오 : ")
for word in name:
    name_in = input(f"{word} : ")
    while True:
        if word == name_in[0]:
            name3.append(name_in)
            break
        else:
            print("첫글자 안맞음. 다시.")
print("*" * 20)
print(f"{name} 이라는 단어로 삼행시를 지어봤어")
for n in range(len(name)):
    print(f"{name[n]} : {name3[n]}")
print("*" * 20)


# f = open("event.txt", "a", encoding = "UTF-8")
# for word in samhaengsi():
#     f.write(word + "\n")
# f.close()