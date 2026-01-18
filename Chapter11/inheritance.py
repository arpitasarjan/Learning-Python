class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = "ITC Infotech"
#     def show(self):show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

    # def showLanguage(self):showLanguage(self):
    #     print(f"The name is {self.name} and he is good with {self.language} language")

class Programmer(Employee):
    pass

a = Employee()
b = Programmer()

print(a.company, b.company)