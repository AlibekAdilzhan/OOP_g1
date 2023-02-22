class Queue:
    def __init__(self, init_items=[]):
        self.items = init_items

    def append(self, a):
        self.items.append(a)

    def pop_front(self):
        self.items.pop(0)

    def __str__(self):
        return f"{self.items}"


q = Queue([1, 2, 3])
q.append(5)
print(q)
q.pop_front()
print(q)
q.append(8)
print(q)
