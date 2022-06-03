# Working with Tabular Data

# import csv

# with open("weather_data.csv") as file:
#   data = csv.reader(file)
#   print(data)
#   temperatures = []
#   for row in data:
#     if data.line_num != 1:
#       temperatures.append(int(row[1]))
      
# print(temperatures)

import pandas as pd 

data = pd.read_csv("./weather_data.csv")

print(type(data)) #2d = Data Frame
print(type(data['temp'])) #1d = Series = List

data_dict = data.to_dict()

print(data_dict)

temp_list = data['temp'].to_list()
print(temp_list)