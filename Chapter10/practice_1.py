class programer:
    company ="Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programer("rk", 1200000, 245001)
print(p.name, p.salary, p.pin, p.company)
r = programer("rohan", 120000, 245001)
print(r.name, r.pin, r.company, r.salary)