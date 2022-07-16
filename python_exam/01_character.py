'''
* 무한반복으로 입력을 받는 프로그램 (while 반복문 + input)
* 좋아하는 게임 캐릭터를 10개까지 받아 리스트에 저장 (list.append)
    - 10개가 넘으면 저장공간이 꽉 찼다며 저장 거부
* 리스트의 내용물을 모두 하나씩 꺼내볼 수 있는 for 반복문
* 리스트의 내용물 중 무작위로 게임 캐릭터 하나를 추천해 줄수 있는 random추천
* 무한반복을 마치는 명령어 입력
* pop 명령어를 이용해 기존의 데이터중 원하는 놈을 삭제하여 공간 확보 (뭘 뺄지 목록 보여주기)
'''
import random
characters = []
running = True

while running:
    character_name = input("좋아하는 캐릭터를 말씀해 주세요 : ")
    if character_name == "목록":
        print("*** 저장된 캐릭터 목록 ***")
        for name in characters:
            print(name)
    elif character_name == "추천":
        recommend = characters[random.randint(0, len(characters))]
        print("{} 캐릭터를 추천드려요".format(recommend))
    elif character_name == "꺼져":
        print("안녕히 가세요 주인님!")
        running = False
    else:
        if len(characters) == 10:
            print("저장공간이 꽉 차서 더이상 캐릭터를 넣을 수 없어요!")
        else:
            characters.append(character_name)