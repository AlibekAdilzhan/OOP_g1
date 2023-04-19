import csv
import random



class App:
    def __init__(self, graph_price, graph_time):
        self.graph_price = graph_price
        self.graph_time = graph_time
        self.users = []

    def dijskstra(self, graph, start, end):
        return 
    
    def register(self, name, surname, login, password, id, money):
        with open("Users.csv", "a", newline="") as fo:
            csv_writer = csv.writer(fo)
            csv_writer.writerow([id, name, surname, login, password, money])
        user = User(name, surname, login, password, id, money)
        self.users.append(user)

    def get_users(self, bd):
        with open(bd, "r") as fo:
            rows = list(csv.reader(fo))
        for row in rows:
            user = User(row[1], row[2], row[3], row[4], row[0], row[5])
            self.users.append(user)

class User:
    def __init__(self, id, name, surname, login, password, money):
        self.id = id
        self.login = login
        self.password = password
    
# s = ""
# for i in range(6):
#     n = random.randint(0, 10)
#     s += str(n)
app = App(None, None)
app.get_users("Users.csv")
login = input("enter login: ")
for u in app.users:
    if u.login == login:
        break

password = input("enter password: ")
if password == u.password:
    print("success")
else:
    print("wrong password")
# name = input()
# surname = input()
# app.register(s, name, surname, "Jeto", "dsjfk", 100500)

