words = ["느금마", "ㄱㅅㄲ", "ㅂㅅ", "ㄲㅈ", "시발", "씨발", "썅", "엄창", "병신", "병1신"]
chat = 0
bad_word = 0
new_word = 0

while True:
    chat = input("코딩쌤>> ")
    bad_word = 0
    if chat == "관리자": # 관리자 모드
        new_word = input("새로운 금칙어를 입력하세요 : ")
        words.append(new_word)
        print(f"{new_word} 단어를 금칙어로 등록했습니다.")
        print(words)
        continue
    for bad in words: #금칙어 대입해 확인하기
        if bad in chat:
            bad_word += 1
    if bad_word > 0:
        print(f"나쁜말 {bad_word}개가 감지되었습니다. 채팅창을 가립니다.")
    else:
        print(chat)