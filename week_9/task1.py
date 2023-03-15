from mw1 import Stack

s = "abcd"

stack = Stack()

for x in s:
    stack.push(x)

for i in range(len(s)):
    print(stack.pop(), end="")