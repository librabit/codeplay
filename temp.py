name = ['김이안','송현수', '송윤수', '정민우', '원동연']
height = [170, 180, 160, 150, 140]

for k in range(5):
    print(f"친구이름 : {name[k]} / 키 : {height[k]}")

max = max(height)
max_idx = height.index(max)
small = min(height)
small_idx = height.index(small)
avr = sum(height) / len(height)
low = []
high = []

high.append()

print("평균키 :", avr)

name[height.index(키)]

print(f"키 젤큰놈 : {name[max_idx]} / {max} \n키 젤작은놈 : {name[small_idx]} / {small}")

# 화면에 아래와 같이 출력하시오
'''
제일 키 큰 친구 : 이름 / 키
제일 키 작은 친구 : 이름 / 키
평균보다 작은 녀석들 : 이름들 (미만)
평균보다 크거나 같은 녀석들 : 이름들 (이상)
'''
for o in range(len(height)):
    if height[o] < avr:
        pass
    else:
        pass