'''
딕셔너리 = 사전.
python의 dictionary = 집합형 자료의 한 종류.

리스트   [] 넣고빼고 삭제 등 데이터 변조가 가능.
튜플    () 데이터 변경이 불가능.
딕셔너리 {} 쌍을 이루는 데이터를 묶어둠.

apple (키 key) <-> 사과 (값 value)
"apple" : "사과"
friend <-> 친구
"friend" : "친구"

sajeon = {"apple" : "사과", "friend" : "친구"}
 
'''

sajeon = {"apple" : "사과", "friend" : "친구", "aori" : "사과"}

print(sajeon["apple"]) #딕셔너리에서 특정한 키를 입력하면 키에 해당하는 값이 반환됨.
print(sajeon["aori"]) # value는 중복이 가능하지만, key는 중복이 안됨.
print(sajeon.keys()) # 딕셔너리에서 키만 추출해 보여줌.
print(sajeon.values()) # 딕셔너리에서 밸류만 추출해 보여줌.
print(sajeon.items()) # 딕셔너리에서 키와 밸류 모두 보여줌.
print("apple" in sajeon) # 특정 키가 있는지 확인.
print("pear" in sajeon) # 특정 키가 있는지 확인.

naver = {"jeongsiu" : ["남자", "양일중", "브롤찐", "자전거", "abcdefg1234"], "kimsunuk" : ["남자", "지평중", "겜알못", "도보"], "kimchiu" : ["남자", "구라중", "탕탕찐", "지하철"]}

if "jungsiwoo" in naver:
    print(naver["jungsiwoo"])
else:
    print("요청하신 찐따는 없어요 ㅋㅋㅋㅋ")

naver["codingssam"] = ["남자", "코드플레이", "개잘생김", "자가용"] # 데이터 추가
# 대상이 되는 딕셔너리에 키 값을 적고, 등호로 건너편에 value에 해당하는 내용을 넣는다.
print(naver)

# del naver["codingssam"] # 특정 데이터 삭제
# del naver["coding3"] # 존재하지 않는 키값 삭제요청

print(naver)

sajeon.update(naver)
print(sajeon)
print(naver)

