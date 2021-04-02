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
* just multiply your random floating number between 0 and 1, by 5. This will include:  $x \in {0,5}$ *(not inclusive)*
