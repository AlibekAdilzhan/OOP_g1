class Teacher:
    def __init__(self, name, id, salary, subject):
        self.name = name
        self.id = id
        self.__salary = salary
        self.subject = subject

    @property
    def salary(self):
        return f"{self.name}'s salary is {self.__salary}"

    @salary.setter
    def salary(self, new_salary):
        self.__salary = new_salary
        print("salary was changed!")


t1 = Teacher("Aaaa", "idq24q234", 100000, "math")
print(t1.salary)
t1.salary = 150000
print(t1.salary)
