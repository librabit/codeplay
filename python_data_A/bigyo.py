import matplotlib.pyplot as plt
import csv

f = open('python_data_A/csv_data/10.csv', 'r', encoding='utf8')
data = csv.reader(f)
result = []
for row in data :
    if '양평읍' in row[0]:
        for i in row[3:]:
            result.append(int(i.replace(",", "")))
        break

print(result)