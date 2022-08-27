ban_dict = ["개새끼", "시팔", "느금마", "병신", "병1신", "ㅂㅅ", "찐따"]
status = True

print("챗봇을 시작합니다!")
while status:
    bad_words = 0
    chat = input("말씀하세요 주인님 : ")
    for word in 순회가능한 데이터 (리스트, 튜플, 딕셔너리, 글자(문자열)): #금칙어 사전에서 검열
        if word in chat:        
            bad_words += 1
    if chat == "꺼져": #챗봇 종료명령 체크
        status = False
    if bad_words == 0: # 금칙어 없을시 대응
        print("맞아요. 주인님.")
    else: # 금칙어 있을시 대응
        print("주댕이에 걸레를 물고잤나. 말 똑바로 해라.")
    
print("안녕히 가세요 주인님. 고맙습니다.")