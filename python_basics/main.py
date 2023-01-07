'''
지금까지 우리가 만든 앱들을 한군데 모아서
한꺼번에 보고 실행할 수 있는 메인파일을 만들자!
(모듈화/패키지화)
1. 단어암기장 = word_input.py
2. 로또번호 추첨기 = lotto_06.py
3. 나쁜말 탐지기 = bad_word.py
4. 계산기 = 03_calculator.py
5. 가위바위보 = rsp.py
'''
from myApps import echo
from myApps import rsp
from myApps import lotto_06 as lt
from myApps import word_input as wi
from myApps import bad_word as bad

select = 0

print("+" * 20)
print("코딩쌤의 앱 모음입니다~")
print("1. 영어단어암기장\n2. 로또번호추첨기\n3. 나쁜말탐지기 \n4. 가위바위보")
print("+" * 20)
select = input("기능을 선택하세요\n => ")
