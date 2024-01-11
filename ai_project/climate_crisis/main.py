data = [0 for _ in range(5)]
print(data)
score = [1, 2, 2, 3, 1, 2, 4, 2, 1, 4, 1, 2, 2, 2, 4, 4, 4, 4, 3]

for i in score:
    data[i] += 1

print(data)

