# 1. HTML의 구조

# 2. 원하는 정보의 위치, 경로

# 3. 크롬에서 원하는 위치정보(경로) 찾기

# 4. Requests

    import requests

    source = requests.get("https://op.gg")
    print("응답코드 : ", res.status_code)

200이 뜨지 않으면 header 정보를 추가해준다.  
문제가 있으면 진행되지만, 없으면 바로 에러를 띄우기만 해도 된다.

    source.raise_for_status() # 문제가 있으면 여기서 멈춤. 없으면 통과.

이 문서를 파일로 만들수도 있다.

    with open("opgg.html", "w", encoding = "utf8") as f:
        f.write(source.text)
