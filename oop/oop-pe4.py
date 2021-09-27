class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# let's make the salary private - so we create an internal private attribute
        self._salary = 6000 
        self._num_bugs_solved = 0
    
    def code(self): 
        #increase number of bugs solved 
        self._num_bugs_solved += 1 

    # making a public function
    # getter
    def get_salary(self):
        return self.salary
    # setter
    def set_salary(self, base_value):
        self._salary = self._calculate_salary(base_value)
# the getter and setter should be the only way to access the private attribute, _salary 

    def _calculate_salary(self, base_value): 
        if self._num_bugs_solved < 10:
            return base_value
        if self._num_bugs_solved < 100: 
            return base_value * 2
        return base_value * 3 

se = SoftwareEngineer('Max', 25)
print(se.name, se.age)
print(se._salary)


for i in range(70): 
    se.code()
