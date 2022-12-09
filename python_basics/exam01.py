'''
1부터 3379까지의 합을 구하시오.

제작시작.
'''
# number = 0
# for i in range(3379):
#     number = number + (i + 1)
#     print(number)
# print(number)


'''
세 개의 리스트를 활용해 무작위로 범인, 범행장소, 범행도구를 조합해
화면에 출력하시오

출력 => ??(이)가 ??에서 ??(으)로 사람을 죽였다
'''

import random
who = ["명석", "지현", "홍석", "서윤"]
where = ["화장실", "교실", "운동장", "편의점"]
what = ["양말", "지우개", "샤프심", "교통카드"]

suspects = [who, where, what]
clues = []
for clue in suspects:
    clues.append(random.choice(clue))

print(f"{clues[0]}(이)가 {clues[1]}에서 {clues[2]}(으)로 사람을 죽임")