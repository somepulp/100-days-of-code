The objects you create are stored in *heap memory* and they have an address which can be accessed with the `id` function:

```
class Computer:
    pass
c1 = Computer()
print(id(c1))
```

Creating another objects takes up a different space in memory. 
What is the size of an object? Who allocates size to object?

- Size depends on the number of variables
- Constructor is responsible to allocate memory. `Computer()` is the constructor - it calls the `__init__` method, whenever its run. 

Self = the current instance or current object being called or referred to. 

Namespace is an area where you create and store an object or variable. 
We have two types of namespaces:
1. Class namespace: you store all the class variables
2. Instance namespace: where you store all the instance variables

Class namespace is shared with the instance namespace since the class variables can be accessed from instances/objects

# Types of Methods
There are different types of methods:
1. Instance methods
2. Class methods
3. Static methods

# Operator Overloading
Addition, subtraction and other operators behave differently depending on the class of the object that it is used on. 
For example, the addition operator '+' is based on the `__add__` method, which is defined differently for each class (ex: string addition = concatenation, while integer addition = aggregation)

We can re-define the __add__ method for a specific class to tell Python what to do when we want to do a class addition. 

For example, for the Student class, which has two initial instance attributes m1, m2, we can define the add behavior to be a sum of the instance attributes for both classes:
```
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
```
Similarly, we can re-define eally any 'pre-defined' operations i'm guessing?
Can redefine:
- `__sub__` = subtract
- __mult__ = multiply
- `__gt__` = greater than
- `__ge__` = greater than or equal to 

printing the class, prints the address of the object. This is disimillar to printing a variable - the value is printed.
When you are printing, a pre-defined method, `__str__` is referred to. For integer/string, print calls `__str__` which returns the values.
We can re-define the `__str__` method within the class to configure what we want to show when the object is printed 

## Method Overloading 
- *not present in python.* 
If you have a class with two methods of the same name or arguments, this is called method overloading