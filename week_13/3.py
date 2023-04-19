import csv

adj_list = {}

with open("data.txt", "r") as fo:
    csv_reader = csv.reader(fo)
    csv_reader = list(csv_reader)[1:]
    for row in csv_reader:
        start = row[0]
        dest = row[1]
        price = row[2]
        dtime = row[3]

        cities = adj_list.get(start, {})
        cities[dest] = [price, dtime]
        adj_list[start] = cities

print(adj_list)
