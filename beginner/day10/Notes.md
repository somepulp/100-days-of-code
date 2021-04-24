Refer to day 6 notes
__________________________

Why use `return` at all? Why not print all the time?

First guess:   
print is of class 'NoneType', so using the result of a function that prints, it may be weird to set it as a variable? 

## Docstrings
- documentation when we are coding.
Tells us what our function is meant to do. To add a docstring, it has to go right below the function declaration, and the documentation should be wrapped in triple quotes:
```
def my_function():
     """ This function will take no inputs, and produce the sum of 2 and 5"""
     return 2+5
```