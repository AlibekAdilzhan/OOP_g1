s = "ab12vs41"
c = 0

for x in s:
    if x.isdigit() == True:
        c = c + int(x)

print(c)