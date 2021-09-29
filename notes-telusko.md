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