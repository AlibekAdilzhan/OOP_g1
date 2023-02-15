class User:
    def __init__(self, name, login, password, age):
        self.name = name
        self.__login = login
        self.__password = password
        self.__age = age

    @property
    def login(self):
        return f"{self.name}'s login is {self.__login}"

    @login.setter
    def login(self, new_login):
        raise AttributeError("you cant change the login")

    @property
    def password(self):
        raise AttributeError("you cant access to password")

    @password.setter
    def password(self, new_password):
        self.__password = new_password
        print("password was changed")


u1 = User("Jack", "Jack003kz", "1324Jjjj", 13)
u1.password = "2384723894732"
