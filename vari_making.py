numbers = 1
varis = []
def char_make(num):
    globals()[f"minion_{num}"] = f"minion{num} created"
    print(globals()[f"minion_{num}"])
    global numbers
    numbers += 1

for i in range(5):
    char_make(numbers)
# print(minion_1)