## Scope

In the starting code, we see the variable `enemies` being accessed within a function and outside a function.
When it is defined within a function, the parameter scope is within that function, so the variable declaration does not over-ride the existing variable which is outside the function.

The `enemies` variable within the function has a local scope, while the `enemies` variable outside of the function has a global scope.

### Local Scope

Local scope exists within functions. Variables defined within functions, such as `my_variable` below, have a local scope. 
```
def my_function():
     my_variable = 5
     print(my_variable)

my_function()
```
This function call will print the value 5. However, if we try to print the variable outside of the function, like so:
```
print(my_variable)
```
This will result in a NameError - because `my_variable` is not defined outside of the function - i.e. it does not have a global scope, thus is inaccessible outside of `my_function()`

### Global Scope 
Variables defined at the top level *(not within a function)* of our programs have global scope and can be accessible anywhere within the program, such as within functions. 
```
var_global = "I'm accessible everywhere"

def second_function():
     print(var_global)
```
This is a valid function call, and `var_global` will be printed when the `second_function()` is called. 


This concept of global and local scoping is not restricted to variables, but also applies to functions and other objects. Basically it applies to anything you *name*. 

This is a concept called **Namespace** - anything you give a name to has a **namespace**. The namespace is valid in certain scopes. 

Whenever you give a name to anything, you must be aware of where you created it, as the namespace will either have 'local' or a 'global' scope and this will certainly affect how you can interact with the object within your programs. 

#### Block Scope

In python, there is no such thing as block scope! This means that if you create a variable within any sort of block of code that is indented, *except for a function*, the variable is not 'fenced' to that block. Meaning that the variable has the same scope as it's enclosing *function*, and if there is no such function, then the variable has _global scope._
```
day = 4
weather = ["Sunny", "Cloudy", "Windy"]
if day != 1:
     day_weather = weather[0]

print(day_weather)
```
Even though the `day_weather` variable is created within the if block, it still has a global scope and can be accessed from outside of that if block.
If this same code is embedded within a function, then we will only be able to access `day_weather`, from *within* the function, because it will not be accessible at the top-level. 

```
day = 4
def weather_selector():
     weather = ["Sunny", "Cloudy", "Windy"]
     if day != 1:
          day_weather = weather[0]

     print(day_weather)
```

### Modifying within a Global Scope

It's not advised to call local variables the same name as with global variables, nor is it a good idea to modify a global variable within a local scope (inside a function).

To access a global variable locally, you must explicitly state that you have a global variable that you want to use within a function:

```
weather = ["Sunny", "Cloudy", "Windy"]

def weather_selector()
     global weather
     weather += ["Overcast"]
     if day != 1:
          day_weather = weather[-1]

     print(day_weather)
```

THIS IS A BAD IDEAAA!!! 

If you really want to modify a global variable, you can do so using the return statement: 
```
weather = ["Sunny", "Cloudy", "Windy"]
def expand_weather():
     print(f"Last weather condition is: {weather[-1]}")
     return weather + ["Overcast"]
```

### Global Constants

These are variables that you define, which you dont plan on changing. The convention in python is to name them in uppercase with an underscore separator. 

```
PI = 3.14159
URL = "https://www.google.com"
```
