# For Loops
General structure: 
```
for item in list_of_items:
    #do something to each item
```
Note that item is equated to the actual element in the list, each time it's 'looped' around. 
    
`item = list_of_items[0]`, ..., 
`item = list_of_items[n-1]`  
*if there are n elements in the list* 

## For loops and the range operator
Sometimes we may want to use a loop completely independent of a list. 

Ex: adding 1 to 100

General structure for range operated for loops:
```
for number in range (x, y, z):
    print(number)
```
where:
- x = starting number (included in the loop)
- y = ending number (excluded from the loop. i.e if y = 10, the loop would count until 10-1 = 9)
- z = step size - counts x + z, up to y

Also note: 
1. We cannot have a step size of zero! 
2. We can count backwards using a negative step size. In order to do this, we require the starting number (x) to be greater than the ending number (y)

Sample: 
```
for number in range(11, 1, -2):
    print(number)
```
This prints out 11, 9, 7, 5, and 3.
\
Remember, it skips the ending number and includes the starting number. 

<img src="https://media.giphy.com/media/dvsgRsiCId0VjLUsSp/giphy.gif" width="150">

Neat!

