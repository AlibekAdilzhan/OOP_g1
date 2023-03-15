class Stack:
    def __init__(self):
        self.elms = []

    def push(self, x):
        self.elms.append(x)

    def pop(self):
        return self.elms.pop()

    def peek(self):
        return self.elms[-1]

    def is_empty(self):
        return self.elms == []



if __name__ == "__main__":
    exp = "[]()[((){)})]"

    sk = Stack()
    parantheses = {"}" : "{", "]" : "[", ")" : "("}
    good = True
    for x in exp:
        if x in {"}", "]", ")"}:
            if sk.is_empty():
                good = False
            elif sk.pop() != parantheses[x]:
                good = False
            
        else:
            sk.push(x)

    print(good)