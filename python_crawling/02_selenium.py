'''
셀레니움은 정적인 웹사이트 데이터를 긁어오는 것이 아니라 직접 브라우저를 컨트롤해 동적으로 데이터를 모을 수 있음.
pip install selenium 으로 셀레니움 모듈 설치
webdriver (셀레니움 모듈과 연동가능한 브라우저 짭)
- 크롬 버전 확인 : 크롬 점세개 매뉴 > 도움말 > chrome 정보
- 버전에 맞는 크롬드라이버 다운로드 : chromedriver_win32.zip
- chromedriver.exe 압축해제
- 크롬드라이버를 현재 작업중인 폴더(지금 있는 파일과 같은 경로)로 옮기기


find_element(By.ID, ‘id’)
find_element(By.NAME, ‘name’)
find_element(By.XPATH, ‘xpath’)
find_element(By.LINK_TEXT, ‘link_text’)
find_element(By.PARTIAL_LINK_TEXT, ‘partial_link_text’)
find_element(By.TAG_NAME, ‘tag_name’)
find_element(By.CLASS_NAME, ‘class_name’)
find_element(By.CSS_SELECTOR, ‘css_selector’)

'''
import time # ?초 기다리기를 위한 모듈
from selenium import webdriver # 크롬 웹드라이버 구동시작
from selenium.webdriver.common.by import By # 크롬드라이버에서 HTML 태그 속 요소를 찾음
from selenium.webdriver.common.keys import Keys # 키보드 입력으로 넘겨줌


browser = webdriver.Chrome()

browser.get("https://www.op.gg/champions")

elem = browser.find_element(By.ID, "searchChampion") # 웹상의 특정한 위치요소 지정
elem.send_keys("아리") # 해당요소에 텍스트 전송
time.sleep(1) # 3초 대기. 웹브라우저가 작동할 시간을 줌.
elem.send_keys(Keys.ENTER) # 해당요소에 특정 키 동작 전송
time.sleep(2)

browser.get("https://www.naver.com")

elem = browser.find_element(By.ID, "query") # 웹상의 특정한 위치요소 지정
elem.send_keys("코드플레이") # 해당요소에 텍스트 전송
time.sleep(1) # 3초 대기. 웹브라우저가 작동할 시간을 줌.
elem.send_keys(Keys.ENTER)
time.sleep(2)

# elem.clear() # 기존에 보낸 내용을 삭제
# elem.send_keys("신지드")


while True: #자동종료 방지
    if "q" == input("quit?"):
        break
