## Dictionaries in Python

Dictionaries in python allow us to group together related pieces of information

Every dictionary has two parts to it: *key* and *value*. \
To make this analogous with a real dictionary, the key would be the word, and value would be the definition of the word. 

To create a dictionary in python, the syntax is as follows: 

`{Key: Value}`
Example: `{"Bug": "An error in a program that prevents it from running as expected."}`

We can have multiple key-value pairs in a dictionary, as follows: 
```
{
     "Key1": "Value1",
     "Key2": "Value2",
     ...
     "KeyN": "ValueN"
}
```
Formatting a dictionary should be as follows:
```
variable_dictionary = {
     "Key1": "Value1",
     "Key2": "Value2"
}
```
- each key-value pair on a different line
- space between first curly brace and first key
- end curly braces in line with beginning of variable name
- commas after values

### Retrieving items from the dictionary

Elements within dictionaries are identified by their key. To extract value2, from our `variable_dictionary`, we would type: 
`variable_dictionary["Key2"]`
We use the keys to retrieve items, thus we have to be careful of typos.

Also note, keys should be provided in their actual data type - so if our key is numeric, we pass a numeric to the square bracket to extract the corresponding value. 

If we want to add a new entry to the dictionary, programatically, we use the following syntax: 
```
variable_dictionary["New_Key"] = "New_Value"
```

We can create an empty dictionary as follows:
```
empty_dictionary = {}
```
We can add to this dictionary by: `empty_dictionary[]=...`

We can edit an item in the dictionary in the same way we would add an item to the dictionary, we'd use an existing key, and change the value by changing the right hand side of the assignment. 
```
variable_dictionary["New_Key"] = "This is a new key"
```

### Looping through a dictionary

Looping through a dictionary, surprisingly, only iterates through the keys
```
for key in variable_dictionary:
     print(key)

## Result: 
Key1
Key2
New_Key
```

Obviously we can use the key in the dictionary to access the values as follows: 
```
for key in variable_dictionary:
     print(variable_dictionary[key])

## Result: 
Value1
Value2
This is a new key
```

## Nesting 

We've seen simple dictionaries, but we can get crazy by making a list or even another dictionary, the value in a dictionary...

![Giirl, my brain hurts](https://media.giphy.com/media/12yo8lScM5oOI0/giphy.gif)

.....wooosahhhh, or whatever beyonce said

![Beyonce](https://media.giphy.com/media/ZBMXbtsbZR5f2/giphy.gif)

<!-- ![oprah_tears](https://media.giphy.com/media/6BNXHG8PeS1xK/giphy.gif)>
<!--![Maan](https://media.giphy.com/media/cmkaW3yTFJ075TwT9o/giphy.gif) -->
<!-- ![](https://media.giphy.com/media/cmkaW3yTFJ075TwT9o/giphy.gif) --> 

This is what nesting is! 

```
{
     Key: [List]
     Key2: {Dict}
}
```
Its more complex, but we are granted more flexibility when storing our data. 

We can nest data as follows:

### 1. List in a dictionary

```
#travel log of cities you've been in each country:
travel_log = {
     "France":["Paris", "Lille", "Dijon"],
     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}
```

### 2. Dictionary in a dictionary
```
travel_log = {
     "France":{
          "cities_visited":["Paris", "Lille", "Dijon"],
          "total_visits": [4,2,2]
     },
     "Germany": {
          "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
          "total_visits": 2
     }
}

```

### 3. Dictionary within a list 
```
travel_log = [
     {
          "country": "France",
          "cities_visited": ["Paris", "Lille", "Dijon"],
          "total_visits": [4,2,2]
     },
     {
          "country": "Germany",
          "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
          "total_visits": 2
     }
]

#Extract France:
travel_log[0]['country']

```