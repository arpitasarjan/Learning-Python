class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def great():
        print("Good morning")

rk = Employee()
# rk.language = "javascript" # This is an instanc attribute
rk.great()
rk.getInfo()
# Employee.getInfo(rk)