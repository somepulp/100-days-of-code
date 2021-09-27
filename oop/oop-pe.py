#Software Engineer list vs class
# position, name, age, level, salary
se0 = ["Software Engineer", "Max", 20, "Junior", 5000]
se2 = ["Software Engineer", "Lisa", 25, "Senior", 7000]

# class
class SoftwareEngineer:
    #class attributes
    alias = "Keyboard Magician"

    # special method to initialize our object
    def __init__(self, name, age, level, salary):
        #instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
    # instance method
    def code(self):
        print(f"{self.name} is writing code...")        
    
    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}...")       
    
    def __str__(self):
        information = f"Name = {self.name}, age = {self.age}, level = {self.level}"
        return information

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    #self is automatically placed in method..
    @staticmethod
    def entry_salary(age): 
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000

# instance
se1 = SoftwareEngineer("Max", 20, "Junior", 5000)
print(se1.name, se1.age)
print(se1.alias)
print(SoftwareEngineer.alias)



# Section 2

se1.code()
se2.code()
se2.code_in_language("Python")
print(se1)

se2 = SoftwareEngineer("Lisa", 25, "Senior", 7000)
se3 = SoftwareEngineer("Lisa", 27, "Senior", 7000)
print(se2==se3)

se3.entry_salary(24)
print(SoftwareEngineer.entrysalary(27))
print(se2.entry_salary(24))
