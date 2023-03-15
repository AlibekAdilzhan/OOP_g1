from mw1 import Stack

sk = Stack()
s = input()

for x in s:
    sk.push(x)

while not sk.is_empty():
    print(sk.pop(), end="")

