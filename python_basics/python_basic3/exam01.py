'''
4명의 용의자, 4개의 범행장소, 4개의 범행도구를 각각 리스트에 담기
각각의 리스트에서 하나의 무작위 용의자, 장소, 도구를 뽑기
뽑은 3개를 하나의 문장으로 아래와 같이 출력하기

"시우"가 "편의점"에서 "느타리버섯"으로 사람을 죽였다!

'''

# import random
# who = ["김시우", "정시우", "김선욱", "송현수"]
# where = ["식당", "청와대", "편의점", "마을버스"]
# what = ["빨대", "교통카드", "지우개", "티스푼"]
# suspects = [who, where, what]
# sageon = []
# for i in suspects:
#     sageon.append(random.choice(i))
# print(f"{sageon[0]}(이)가 {sageon[1]}에서 {sageon[2]}(으)로 사람을 죽였다!")


'''
1부터 1234까지 수를 모두 더하시오
'''
def deotsem(number):
    sum = 0
    for i in range(number):
        sum += (i + 1)
    print(sum)
    return sum

print(deotsem(15))