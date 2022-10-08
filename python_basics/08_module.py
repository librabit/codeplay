import random
from split_04 import *
from lotto_06 import lotto1
import fortuneteller_07 as ft

select = 0

running = True
while running:
    select = int(input('''안녕하세요 주인님. 무엇을 실행할까요?
1. 계산기   2. 로또번호 추첨기   3. 미래배우자 알리미  4. 끝
(위의 앱 중 하나를 번호로 선택하세요) : '''))
    if select == 4:
        break
    elif select == 2:
        lotto1()
    elif select == 1:
        ft.future()
    elif select == 1:
        print(myname)
        calculator()

print("주인님 오늘도 행복한 하루되세염~")