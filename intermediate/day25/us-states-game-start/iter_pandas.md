# Iterating through DataFrames with Pandas

We can iterate through dataframes, similar as we would with dictionaries, using `.iteritems()` and `.iterrows()` methods

```python

student_dict = {
    'student': ["Angela", "James", "Lily"],
    'score': [56,76,98]
}

student_data = pd.DataFrame(student_dict)
print(student_data)
```
Recall dictionary iteration syntax:

```python
for k,v in student_data.items():
    print(v)
```

## Iterating through pandas columns and series values

```python
for column,lst in student_data.iteritems():
#     #print(column, lst)
    print(column)
    print(lst)
```

## Iterating through pandas indices and row values

```python
for index,row in student_data.iterrows():
    # print(index,row)
    # print(index)
    print(row)
```