class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language): # Dunder method which is automatically caled
        self.name = name
        self.salary = salary
        self.language = language
        print(" I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
        
    @staticmethod
    def great():
        print("Good Morning")


rk = Employee("rk", 1300000,"Javascript")
# rk.name ="rk"
print(rk.name,rk.salary)
