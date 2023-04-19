import csv
from pprint import pprint

adj_list = {}
cities = set()

with open("data.txt", "r") as fo:
    csv_reader = csv.reader(fo)
    data = list(csv_reader)[1:]
    for row in data:
        cities.add(row[0])
        cities.add(row[1])

cities = sorted(list(cities))
print(cities)

adj_matrix_1 = [[0] * len(cities) for _ in range(len(cities))]
adj_matrix_2 = [[0] * len(cities) for _ in range(len(cities))]

for row in data:
    i = cities.index(row[0])
    j = cities.index(row[1])
    adj_matrix_1[i][j] = int(row[2])
    adj_matrix_2[i][j] = int(row[3])


for row in adj_matrix_2:
    print(row)

# print(adj_matrix)

# adj_matrix = []