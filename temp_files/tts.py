import pyttsx3
import re

# TTS 엔진 초기화
engine = pyttsx3.init()

# 사용 가능한 음성 엔진 목록 가져오기
voices = engine.getProperty('voices')

# 영어 음성 엔진 선택
eng_engine = None
for voice in voices:
    if "english" in voice.name.lower():
        eng_engine = voice
        break

# 한국어 음성 엔진 선택
kor_engine = None
for voice in voices:
    if "korean" in voice.name.lower():
        kor_engine = voice
        break

# 입력 받기
text = input("입력하세요: ")

# 영어와 한글 부분 구분
eng_text = re.sub(r'[ㄱ-ㅎ가-힣]+', '', text)
kor_text = re.sub(r'[a-zA-Z]+', '', text)

# 영어 부분 출력
if eng_text:
    engine.setProperty('voice', eng_engine.id)
    engine.say(eng_text)
    engine.runAndWait()

# 한글 부분 출력
if kor_text:
    engine.setProperty('voice', kor_engine.id)
    engine.say(kor_text)
    engine.runAndWait()