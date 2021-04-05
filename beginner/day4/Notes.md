# Day 4 Lessons
## Randomization 
This is important for computer programs that need some unpredictability
(essential for games).


How do we create *randomness* for our programs? 

Computers and machines are deterministic - they perform repeatable actions in predictable ways. How do we wrangle these deterministic machines to get them to produce randomized results? 

There are pseudo-random number generators, and math theory involved in doing this.

Practically, we can get random numbers in less *complicated* ways. 

Using the search engine on [AskPython.com](askpython.com) - look for the *random module*. You will find [documentation](https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences) that contains functions which enable you to generate random numbers

To use the random module we must import the package into our python program as follows:

```
import random
```
Sample functions to use: 
```
random.randint(a,b)
```
- this generates a random integer between a and b (inclusive)

_________

Hold up, wait a minute!
We've just been introduced to modules. So, what is a module?

![Alt Text](https://media.giphy.com/media/aWU9OI9oxxwGc/giphy.gif)

<!-- <img src="https://media.giphy.com/media/aWU9OI9oxxwGc/giphy.gif" width="250">
-->
Welll

At times code gets really complicated and it gets harder to understand what your code is doing in a very long script. 
A solution is to split up  the code into individual modules where each module is responsible for different functionalities within your program.
For complex projects with many modules, this segmentation enables you to collaborate easier with others as different people could be working on different functionalities separately. 

So a module is a collection of code/functions that accomplish a specific goal or provide a specific functionality that can be used or slotted into other bodies of code. 

Essentially, its functional-piece-wise code. 

How can we create our own modules? 
It's as easy as creating other .py files and importing it into another script (in the same folder/location)

We'll create a module which contains some digits of pi, called `pi_module.py`. Since this is saved in the same location as our main script `day4.py`, we can run the following code to use our *module*:
```
import pi_module
```

Back to random numbers, we can return random floating point numbers using the module:  `random.random()` 
This will generate a floating point number between 0 and 1

How do we create a random decimal number between 0 and 5?
* just multiply your random floating number between 0 and 1, by 5. This will include numbers between 0 and 5 *(not inclusive)*

----
## Lists

Lists are just one of the ways to organize and store data (data structure)
- good for grouped pieces of data, which have a connection with each other.
- ex: storing names of states - they 'belong' together, so might want to store this is one variable

Lists are just a set of *square brackets*, separated by commas:
```
fruits = ["banana", "orange"]
```

Within lists, we can have different data types, i.e a list can contain booleans, integers, strings, floats, at the same time.

Ordering within the list is important as items can be extracted based on their position in the list. 
*Note*: zero-indexing applies to lists as well (previously we saw this when extracting characters from strings)

In addition to positive indexing, we can also use negative indexes. We start with -1 as the last item in the list (-0 means nothing in math).

Lists are also **mutable**. 

We can change items in the lists through indexing as follows:
```
states_of_america[1] = "Alaska"
```

This would keep the other items in the list the same, but replace *Pennsylvania* with *Alaska*.


We can also add items into the list using the *append* function: 
```
states_of_america.append("Arkansas")
```
This will add "Arkansas" to the end of our `states_of_america` list. 

We can extend a list (add another list to the end of it) by using the *extend* function: 
```
states_of_america.extend(["Minnesota", "California"])
```

Other lists functions are included in the python documentation [here](https://docs.python.org/3/tutorial/datastructures.html).

