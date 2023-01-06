'''
파일을 만들고, 읽고, 쓰고, 불러오기.
'''
f = open("test.txt", "a", encoding = "UTF-8")
# f = 객체
# 파일을 새로 만들거나, 있는 파일을 덮어쓸때는 "write"
# 기존 파일에 내용을 덧붙일때는 "add"
# 기존 파일에서 내용을 읽어오기만 할 때는 "read"

f.write("집중해라오씨최씨"+"\n")
f.write("아까 내가 명석이 용돈줬다"+"\n")
f.write("끝나고 명석이한테 먹을거 사달라해"+"\n")
# w나, a로 파일에 쓰기가 가능할 때 write 매서드로 내용 적을 수 있음.
f.close()

f = open("test.txt", "r", encoding = "UTF-8")
line = f.readline()
lines = f.readlines()
print(line)
print(lines)
f.close()
# 불러온 파일을 닫아줌
