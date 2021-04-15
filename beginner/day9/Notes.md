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