# 아나콘다 : 개발환경의 다양한 라이브러리 관리
import google.generativeai as ai
import PIL.Image


GOOGLE_API_KEY = "AIzaSyBI6uCA4UOTchGCgYSuwGlc-msA8Ul6-UA"

ai.configure(api_key=GOOGLE_API_KEY)

model = ai.GenerativeModel('gemini-1.5-flash')

chat =  model.start_chat(history=[
    {
        'role':'user',
        'parts':["문장의 숨겨진 의미를 해석하고 적절한 행동을 간단하게 제안하세요. ASD를 가진 사람들에게 40자 이내로 제안하세요. 숨겨진 의미가 문자 그대로의 의미와 다를 경우에만 해석하세요. 결과는 \"숨은 의미: ~\n추천 행동: ~\" 형식으로 출력하세요. 숨겨진 의미가 없으면 \"숨은 의미: 없음\n추천 행동: ~\" 형식으로 출력하세요."]
    },
])

def aichat(message):
    res = chat.send_message(message)
    return res.text

while True:
    message = input("Me: ")
    if message == 'q':
        print("Bye!")
        break
    response = aichat(message)
    print("AI:", response)
