# Types of methods

class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def __str__(self):
        information = f"Name = {self.name}, Rollno = {self.rollno}"
        return information
    
    class Laptop:
        
        def __init__(self) -> None:
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8


s1 = Student("Joy", 1)
s2 = Student("Gloria", 2)

print(s1)
s1.lap.brand

## Operator overloading

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
    
    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False
    