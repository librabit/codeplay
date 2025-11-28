# 0. 어떻게 해결할 지 머릿속으로 알고리즘을 생각해 본다.
#  - 월요일부터 금요일까지 반복해 비교해본다
#     - 요일별로 세 가지 조건을 비교해 본다
#     - 세 가지 조건 중 어느 하나라도 맞지 않으면 그 날은 축구를 못한다
#  - 일주일 내내 아예 축구를 못하는 날은 -1을 기록한다.
#  - 축구를 할 수 있는 날은 그날의 요일을 한 칸씩 띄어쓰기해 알려준다.

# 1. 필요한 데이터를 정리한다.

#     1-1. 주어진 데이터를 처리가능하도록 변환
#     1-2. 주어지지 않은 데이터 중 추가로 생성해야 하는 데이터를 정리
2. 앞에서 생각한 알고리즘을 코드로 구현한다.
3. 원하는 조건으로 결론을 제출한다.

weather = list(map(int, input().split()))
wind = list(map(int, input().split()))
book = list(map(int, input().split()))

yoil = ["Mon", "Tue", "Wed", "Thu", "Fri"]
OK = []
res = ""

for i in range(5):
    if weather[i] == 0 and wind[i] < 20 and book[i] == 0:
        OK.append(yoil[i])

if len(OK):
    res = " ".join(OK)
else:
    res = -1
    
print(res)
