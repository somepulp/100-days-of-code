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
