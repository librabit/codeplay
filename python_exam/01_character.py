import random

character = []
running = True

while running:
    data = input("좋아하는 캐릭터를 말해보세요 : ")
    if data == "끝":
        print("수고하세요!")
        running = False
    elif data == "추천":
        print(f"{character[random.randint(0, len(character)-1)]} 캐릭터를 추천드려요")
    elif data == "항목":
        print(f"지금까지 입력된 캐릭터는 {len(character)}개 입니다.")
        print("각각의 캐릭터는 아래와 같습니다")
        for character_name in character:
            print(character_name)
    else:
        if len(character) > 10:
            print("저장공간이 꽉찼어요!")
        else:
            print(f"{data}캐릭터를 추가하였습니다")
            character.append(data)
