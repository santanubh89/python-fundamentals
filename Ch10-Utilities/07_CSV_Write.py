import csv

output_file = open('output.csv', 'w', newline='')
print(type(output_file))
writer = csv.writer(output_file, delimiter='\t')
writer.writerow(['Name', 'Hours', 'Rate'])
writer.writerow(['Foo', '10', '1000'])
writer.writerows([['Bar', '12', '600'], ['Bar', '12', '600']])
output_file.close()