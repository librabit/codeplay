# 🎓 처음 배우는 파이썬 - 단계별 실습 문제
# 구글 Colab에서 실행할 수 있어요!

"""
처음부터 끝까지 직접 작성하는 문제 (3개)
"""

# 문제 1: 문방구 영수증 만들기 🏪
"""
문방구에서 물건을 산 후 영수증을 만들어봅시다.
연필 한 자루는 500원, 지우개 한 개는 300원입니다.

[힌트]
1. 변수는 아래 이름을 사용해보세요:
   - pencil_price: 연필 가격
   - eraser_price: 지우개 가격
   - pencil_count: 구매한 연필 개수
   - eraser_count: 구매한 지우개 개수
   - total_price: 총 금액

2. 사용할 문법:
   - 변수 = 숫자  (예: pencil_price = 500)
   - input() 함수로 개수 입력받기
   - int() 함수로 입력값을 숫자로 변환
   - print() 함수로 결과 출력하기
   - 덧셈(+)과 곱셈(*) 연산자
"""

pencil_price = 500  # 연필 가격
eraser_price = 300  # 지우개 가격

print("=== 문방구 영수증 만들기 ===")
pencil_count = int(input("연필은 몇 자루 구매하셨나요? "))
eraser_count = int(input("지우개는 몇 개 구매하셨나요? "))

total_price = (pencil_price * pencil_count) + (eraser_price * eraser_count)

print("\n=== 영수증 ===")
print(f"연필 {pencil_count}자루 X {pencil_price}원 = {pencil_price * pencil_count}원")
print(f"지우개 {eraser_count}개 X {eraser_price}원 = {eraser_price * eraser_count}원")
print(f"총 금액: {total_price}원")


# 문제 2: 오늘의 날씨 ⛅
"""
오늘 아침, 점심, 저녁 기온을 입력받아
평균 기온과 일교차를 계산해보세요.

[힌트]
1. 변수 이름:
   - morning: 아침 기온
   - afternoon: 점심 기온
   - evening: 저녁 기온
   - average: 평균 기온
   - highest: 가장 높은 기온
   - lowest: 가장 낮은 기온
   - difference: 일교차

2. 사용할 문법:
   - input()으로 기온 입력받기
   - int()로 숫자로 변환
   - max() 함수로 가장 높은 기온 찾기
   - min() 함수로 가장 낮은 기온 찾기
   - 나눗셈(/) 연산자로 평균 계산하기
   - round() 함수나 :.1f로 소수점 한 자리까지 표시
"""

[이하 코드 동일...]

# 문제 4: 준비물 체크하기 ✅
"""
준비물 리스트를 보고 
잊은 물건이 있는지 체크해봅시다.

[힌트]
1. 리스트에 있는지 확인하기:
   if 물건 in 리스트:
       있다고 출력
   else:
       없다고 출력

2. 사용할 문법:
   - in 연산자로 리스트 안에 있는지 확인
   - if-else 문으로 조건 분기
"""

[이하 유사한 형식으로 각 문제에 힌트 추가...]

# 문제 6: 피구 팀 정하기 ⚾
"""
학생 8명을 두 팀으로 나누어 피구를 하려고 합니다.
출석번호 1번부터 8번까지 있을 때, 
짝수 번호와 홀수 번호로 팀을 나눠보세요.

[힌트]
1. 변수 이름:
   - students: 전체 학생 번호 리스트
   - team_a: A팀 학생들의 번호
   - team_b: B팀 학생들의 번호

2. 사용할 문법:
   - % 연산자로 짝수/홀수 구분하기 (숫자 % 2 == 0 이면 짝수)
   - append() 함수로 리스트에 추가하기
   - if-else 문으로 조건 분기

3. 알고리즘 힌트:
   - 학생 번호가 짝수면 team_a에 추가
   - 학생 번호가 홀수면 team_b에 추가
"""

[이하 코드는 동일하게 유지...]
