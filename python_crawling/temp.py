from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# ChromeDriver 경로 설정
browser = webdriver.Chrome(ChromeDriverManager().install())

# Naver 웹 페이지 열기
browser.get('https://www.naver.com')

# '웹툰' 텍스트 링크 찾아서 클릭
webtoon_link = browser.find_element(By.LINK_TEXT, '웹툰')
webtoon_link.click()

time.sleep(3)
# 브라우저 닫기
browser.quit()