class Employee:
    language = "Python" # This is a class attribute
    salary = 1300000

rk = Employee()
rk.language = "Javascript" # This is an instance attribute
print(rk.language, rk.salary)