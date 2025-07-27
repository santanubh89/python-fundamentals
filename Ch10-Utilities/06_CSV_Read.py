import csv

data = open('employee.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_object = list(csv_data)

print(f'CSV Data = {data_object}')
#del data_object[0]
for index, [name, hours, rate] in enumerate(data_object):
    if index == 0:
        continue
    print(f'Index = {index}, Name = {name}, Hours = {hours}, Rate = {rate}')
