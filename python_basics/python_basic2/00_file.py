'''
파일을 만들고, 읽고, 쓰고, 불러오기.

f = 객체
파일을 새로 만들거나, 있는 파일을 덮어쓸때는 "write"
기존 파일에 내용을 덧붙일때는 "add"
기존 파일에서 내용을 읽어오기만 할 때는 "read"

'''
        # 열 파일 / 어떤 모드로 열까? /  글씨저장방식
# f = open("test.txt","a", encoding = "UTF-8") # w나, a로 파일에 쓰기가 가능할 때 write 매서드로 내용 적을 수 있음.
# for name in range(10):
#     name = input("이름입력 : ")
#     f.write(name + "\n")
# f.close()

f = open("test.txt", "r", encoding = "UTF-8")
# line = f.readline()
lines = f.readlines()
# print(line)
print(lines)

for i in range(len(lines)):
    lines[i] = lines[i].strip()

print(lines)

f.close() # 불러온 파일을 닫아줌

# C:\Users\librabit\Documents\++++python_class\python_basics\python_basic2\00_file.py
