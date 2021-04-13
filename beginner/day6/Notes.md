## Functions

In-built python functions work similarly - inputs go within the parentheses.

To make our own functions we need to use the `def` keyword. Think of this as *def*ining your function. The general structure is below:
```
def function_name():
    do something
```
To call the function, type: `function_name()` - add any necessary inputs within the parentheses. 

Functions give us a way of minimizing repetitive code, or re-using it efficiently. 
Rather than having to type and retype the same set of instructions, turn it into a function! 
Simplify yo life!!

![Oprah breathing](https://media.giphy.com/media/26n6GY1gFUUzVLrR6/giphy.gif)


## Indentation 

Indentation is super important in python. Anything idented within the function is considered as a code block, and ran within the function. 

If code is indented at the same level as the function definition, then that piece of code is considered to NOT be within the function. So when the function is called, that piece of code will not be ran. 

Same thing applies, as usual for ifelse statements, loops, etc. 

Note: the official python documentation defines an indent as 4 spaces, so ensure your editor converts tabs to 4 spaces!

______________

## While Loops
The general structure of a while loop is as follows: 

```
while something_is_true:
    do something repeatedly
```
The loop only stops when the condition becomes **FALSE**

From the hurdles exercise, we can acheive the same functionality using a while loop as follows: 

```
while number_of_hurdles > 6:
    jump()
    number_of_hurdles += 1
```

Alternatively, if we have a function which checks whether or not the robot is at the goal, we can modify the while loop as follows: 

```
while not at_goal():
    jump()
```

### When would you use a for loop vs a while loop?

For loops are great when: 
- iterating over something and performing operations with each element being iterated over 

Ex: iterating over a list and performing an operation, such as `print()` for each element in the list. 

While loops are for when:
- the position in the item being iterated over is irrelevant. 
- want to carry out a functionality many times, until a set condition becomes **False**.
Ex: You dont care about the position in a sequence, you just want to run a function until a condition is negated.  

#### Infinite Loops
While loops run based on the condition - as long as it is not False, the loop continues to run.
For loops, on the other hand, have a natural stopping point. Ex: the end of the list (or other data structure), or the end of the range.   

While loops can create *infinite loops* if the condition never becomes False. This is problematic because of finite resources - think of all the RAM this would eat up. 

Therefore, you must be careful when creating a while loop to ensure that you have an appropriate condition which is not always True. 
If you dont know why you have an infinite loop, print out your condition at each iteration to see whether it can even change. 

__________
## Functions With Inputs
To create a function that depends on inputs from the user, all you need to do is include parameters in the function definition, like so:
```
def my_function(parameter):
    Do something with parameter
    Do something else
    etc...
```

You can include as many parameters as you want. Also you can make certain parameters default to a certain value, if the user does not input anything:

``` 
def weather_check(city, night = FALSE):
    #check city weather on website, when it is not night
    #if night = TRUE, check city weather on website for nighttime 
```

Note that when we call a function which expects inputs, we have to understand two concepts:
- parameters: the name of the inputs that the function expects. In our previous function, the parameters are `city` and `night`
- arguments: the actual value being passed to the function when it's being called. 


Also note: the position of arguments matter, unless you explicitly associate the arguments with the parameter like so: 
```weather_check(night=FALSE, city="Caledon")```

