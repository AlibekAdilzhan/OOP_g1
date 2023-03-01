class Queue:
    def __init__(self):
        self.elms = []

    def append(self, x):
        self.elms.append(x)

    def pop_front(self):
        # if self.is_empty():
            # raise AttributeError("there are no elements in the queue")
        return self.elms.pop(0)

    def is_empty(self):
        if self.elms == []:
            return True
        else:
            return False

    def peek(self):
        return self.elms[0]
    
    def size(self):
        return len(self.elms)

    def __str__(self):
        return f"{self.elms}"


n = 5
q = Queue()
q.append("1")
for i in range(n):
    a = q.pop_front()
    new_a1 = a + "0"
    new_a2 = a + "1"
    q.append(new_a1)
    q.append(new_a2)
    print(a, end=' ')