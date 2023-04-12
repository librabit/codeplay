# 장소 검색하기

# from PyKakao import Local

# # Daum 검색 API 인스턴스 생성
# LOCAL = Local(service_key = "5b325261dea4053351cd099ed2b4567c")

# df =  LOCAL.search_keyword("판교역", dataframe=False)

# print(df)



# 다음 검색하기

# from PyKakao import DaumSearch

# # Daum 검색 API 인스턴스 생성
# DAUM = DaumSearch(service_key = "5b325261dea4053351cd099ed2b4567c")

# # 웹문서 검색
# df = DAUM.search_web("김건희 특검", dataframe=True)

# print(df)



# 카카오톡으로 문장 생성하기

from PyKakao import KoGPT

# KoGPT API 인스턴스 생성
GPT = KoGPT(service_key = "5b325261dea4053351cd099ed2b4567c")

# 다음 문장 만들기
prompt = input("시작말을 써라 : ")
max_tokens = 64
result = GPT.generate(prompt, max_tokens, temperature=0.7, top_p=0.8)

result_list = list(result.values())
refine = list(result_list[1][0].values())

munjang = refine[0].split(".")
# for rm in munjang:
#     if rm == "":
#         munjang.remove(rm)
# print(munjang)

for i in range(len(munjang) - 1):
    print(munjang[i])




# 카카오톡으로 나에게 메시지 보내기

# from PyKakao import Message

# # 메시지 API 인스턴스 생성
# MSG = Message(service_key = "5b325261dea4053351cd099ed2b4567c")

# # 카카오 인증코드 발급 URL 생성
# auth_url = MSG.get_url_for_generating_code()
# print(auth_url)


# answer = input("url 복사후 붙여넣으시오 \n=>")


# # 카카오 인증코드 발급 URL 접속 후 리다이렉트된 URL
# url = answer

# # 위 URL로 액세스 토큰 추출
# access_token = MSG.get_access_token_by_redirected_url(url)

# # 액세스 토큰 설정
# MSG.set_access_token(access_token)

# # 텍스트 메시지 전송


# text = input("보낼 메시지 : ")
# link = {
#             "web_url": "https://developers.kakao.com",
#             "mobile_web_url": "https://developers.kakao.com"
#         }
# button_title = "바로 확인"

# MSG.send_text(text=text, link={}, button_title=button_title)


