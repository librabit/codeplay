bad_words = ["병신", "븅신", "찐따", "빡빡이", "대머리", "느금마", "ㅈㄹ", "지랄", "ㅄ", "ㅅㅂ"]
bad_word = []
answer = 0
add_word = 0

def bads():
    while True:
        answer = input("말씀하세요 주인님 : ") # 채팅 입력
        bad_word = [] # 나쁜말 바구니 비우기
        for word in bad_words: # 채팅에 나쁜말 사전을 하나씩 넣어서 나쁜말 했나 확인
            if word in answer:
                bad_word.append(word) # 나쁜말 했으면 나쁜말 바구니에 넣어두기
        if len(bad_word) > 0: # 나쁜말 바구니에 하나라도 들어있으면 아래 실행
            print(f"{bad_word} <- 이런 말은 쓰면 안돼요. 나빠요. 샹놈아") # 나쁜말 바구니 보여주고 욕함
            continue
        else:
            if answer == "꺼져":
                print("안녕히 가세요 주인님!")
                break
            elif answer == "추가":
                add_word = input("어떤 단어를 추가할까요? : ")
                bad_words.append(add_word)
                print(f"{add_word} 단어가 금칙어에 추가되었습니다")
                print(f"지금까지 등록된 금지단어를 보여드릴께요")
                print("=" * 50)
                print(bad_words)
                print("=" * 50)
                continue
            else:
                print(f"{answer} (이)라구요? 옳은 말씀이십니다 주인님")