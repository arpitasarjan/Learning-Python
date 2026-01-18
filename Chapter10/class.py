class Employee:
    language = "python" # This is a class attribute
    salay = 1200000


rk = Employee()
rk.name = "rk" # This is a instance attribute
print(rk.name, rk.language, rk.salay)

rahul = Employee()
rahul.name = "Rahul K "
print(rahul.name,rahul.salay, rahul.language)

# Here name is insatance attribute and salay and language attributes as they directly belong to the class