with open("data.txt", "r") as fo:
    lines = fo.readlines()

lines = [line.strip().split(",") for line in lines]
lines.pop(0)
cities_1 = [line[0] for line in lines]
cities_2 = [line[1] for line in lines]

cities = cities_1 + cities_2
cities = list(set(cities))
print(sorted(cities))
