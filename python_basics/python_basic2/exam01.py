'''
1번 문제.

범인과 범행장소, 범행도구를 만들고
무작위로 세 가지 요소를 뽑아서
아래의 예시처럼 출력하시오

"재성"이가 "편의점"에서 "양말"로 사람을 죽임

범인은 4명
장소도 4곳
도구도 4개
를 리스트로 작성하셔서 진행하세요


2번 문제.

1부터 4856까지의 합을 구하시오.
코드로 계산식을 만들어서 구하시오.

'''

# import random
# who = ["재민", "재성", "율", "사온"]
# where = ["안방", "3반 교실", "청와대", "수리남"]
# what = ["안농운가발", "슬리퍼", "코딱지", "숫가락"]
# murder = [who, where, what]
# result = []
# for i in murder:
#     result.append(random.choice(i))
# print(f"{result[0]}(이)가 {result[1]}에서 {result[2]}(으)로 사람을 죽임. 대박사건")




# 1부터 5까지 더하는 공식을 만들어봅시다.
# 1~5를 모두 더하면 15.

def add(num):
    result = 0
    for number in range(num): #0, 1, 2, 3, 4가 차례대로 number에 대입
        result += (number + 1)
    return result

print(add(4856))
