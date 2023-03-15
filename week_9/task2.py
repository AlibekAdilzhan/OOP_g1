from mw1 import Stack

exp = "([)]"

d = {")": "(", "]": "[", "}" : "{"}

sk = Stack()
good = True
for x in exp:
    if x in {"(", "[", "{"}:
        sk.push(x)
    else:
        if sk.is_empty():
            good = False
        elif sk.pop() != d[x]:
            good = False
            break


print(good)