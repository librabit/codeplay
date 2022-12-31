'''
변수X / 객체object open = class
쓰기 (w = write / a = add) 읽기 (r = read)
'''
f = open("test.txt", "r", encoding = "UTF-8")
print(f.readline())
words = []
for remove in f.readlines():
    words.append(remove.strip())
print(words)
f.close()