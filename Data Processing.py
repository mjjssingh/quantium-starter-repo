from re import sub
import csv


def findSales(path):
    file = open(path, 'r')
    reader = csv.reader(file)
    print(next(reader))
    for line in reader:
        if line[0] == key:
            row = []
            price = float(sub(r'[^\d.]', '', line[1]))
            quantity = int(line[2])
            sales = price * quantity
            row.append("${:.2f}".format(sales))
            row.append(line[3])
            row.append(line[4])
            writer.writerow(row)


path1 = "data/daily_sales_data_0.csv"
path2 = "data/daily_sales_data_1.csv"
path3 = "data/daily_sales_data_2.csv"

output = open("output.csv", 'a', newline='')
writer = csv.writer(output)
writer.writerow(['Sales', 'Date', 'Region'])
key = "pink morsel"

findSales(path1)
findSales(path2)
findSales(path3)
