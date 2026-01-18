class Employee:
    def __init__(self):
        print("Constructor of Employee")
        self.a = 1

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer")
        self.b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
        self.c = 3

o = Manager()
print(o.a, o.b, o.c)
