'''
현관문 도어락 만들기 1

1. 초기 비밀번호를 0000으로 입력한다.
2. 초기 비밀번호를 입력하고 문을 열면 새로운 비밀번호를 등록하라고 지시한다.
 2-1. 비밀번호는 2번 입력해서 둘 다 일치해야 새로운 비번으로 등록해줌.
3. 그 다음부터는 새로운 비밀번호를 입력해야 문이 열린다.
4. while True 반복문으로 계속 작동하게 한다.
5. 비밀번호가 틀렸으면 틀렸다고 말해준다.


현관문 도어락 만들기 2
1. 기존의 비밀번호를 변경할 수 있는 메뉴를 넣으시오.
 1-1. 기존 비번을 변경하기 위해서는 현재비번도 체크해야 함.
2. 비밀번호 안심기능을 통해, 비밀번호 이외에 다른 숫자들을 더 넣어도 비밀번호가 포함되면 열리게 해주시오.


현관문 도어락 만들기 3
1. 현관문에는 배터리가 들어있다.
2. 배터리의 최초 용량은 100이다.
3. 문이 한 번 열릴때마다 3~5만큼 배터리가 닳는다.
4. 배터리가 20% 이하일때 배터리 경고를 낸다.
5. 배터리 경고가 나올 때만 배터리 교체기능을 넣어준다.
6. 계속 배터리를 안갈아서 배터리가 0 이하이면 반복문을 종료한다.
'''
import random

pw = "0000" # 기기에 저장된 비번
ppww = "" # 여러분이 입력하는 비번
temp_pw = "" # 비번 변경시 2번째 입력 담아두는 임시 비번
battery = 100

def change_pw(pw1, pw2):
    while pw1 != pw2:
        pw1 = input("새로운 비번을 입력하시오 : ")
        pw2 = input("한번 더 입력하시오 : ")
        if pw1 == pw2:
            print("비밀번호 변경이 완료되었습니다")
            return pw1
        else:
            print("비밀번호가 일치하지 않습니다. 다시 비번변경 해주세요.")
def bt():
    global battery
    bt = random.randint(23, 35)
    if battery <= 20:
        answer = input("배터리를 교체하실래요? y/n ")
        if answer == "y":
            battery = 100
    battery -= bt
    print(battery)

while battery > 0:
    ppww = input("비번을 입력해라 (비번변경 - c): ")
    if pw in ppww:
        if pw == "0000":
            pw = change_pw(ppww, temp_pw)
        else:
            print("문이 열렸습니다")
            bt()
    elif ppww == "c":
        ppww = input("기존 비번을 입력하시오 : ")
        if pw in ppww:
            pw = change_pw(ppww, temp_pw)
        else:
            print("비번 틀림")
    else:
        print("비번이 틀렸다")

print("배터리 소진으로 도어락 작동이 중지되었습니다")

