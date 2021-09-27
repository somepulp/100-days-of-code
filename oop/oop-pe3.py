# inherits, extend, override

class Employee: #parent class
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working...")

class SoftwareEngineer(Employee): #child class inheriting from Employee class (parent)
    
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level
    
    def debug(self):
        print(f"{self.name} is debugging...")

    def work(self):
        print(f"{self.name} is coding...")

class Designer(Employee): #child class

    def draw(self):
        print(f"{self.name} is drawing...")

    def work(self):
        print(f"{self.name} is designing...")

employ = Employee("Janet", 30, 100000)
se = SoftwareEngineer("Joy", 27, 175000, "Senior")
print(se.name, se.age)
#se.work()

de = Designer("Phil", 27, 120000)
print(de.name, de.age)
#de.work()

# Polymorphism
employees = [Employee("Max", 25, 6000),
             SoftwareEngineer("Lisa", 30, 9000, "Senior"),
             Designer("Phillip", 27, 7000)]
            
def motivate_employees(employees):
    for employee in employees:
        employee.work()

motivate_employees(employees)
