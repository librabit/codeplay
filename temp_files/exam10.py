#141
리스트 = [100, 200, 300]
for i in 리스트:
    print(int(i*1.1))

#142

#160
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']

for f in 리스트:
    ff = f.split('.')
    print(ff[0])

for i in 리스트:
    t = ""
    for j in "intra.h":
        if j == ".":
            break
        t += j
    print(t)

for f in 리스트:
    ff = f.split('.')
    if ff[1] == "c" or ff[1] == "h":
        print(f)

for j in 리스트:
    if ".c" in j or ".h" in j:
        print(j)

