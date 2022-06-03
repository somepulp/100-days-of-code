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

# print(type(data)) #2d = Data Frame
# print(type(data['temp'])) #1d = Series = List

# data_dict = data.to_dict()

# print(data_dict)

# temp_list = data['temp'].to_list()
# print(temp_list)

# avg_temp = sum(temp_list)/len(temp_list)

# import statistics

# avg_temp2 = statistics.mean(temp_list)

# print(avg_temp, avg_temp2)

# print(data['temp'].mean())
# print(data['temp'].max())

# # Getting data in columns
# print(data['condition'])
# print(data.condition)
# print(data['day'])
# print(data.day)
# print(data.temp)


# # Getting data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])


# # Getting cell
# monday = data[data.day == "Monday"]
# print(monday.condition)

# monday_tempF = (monday.temp*9/5) + 32
# print(monday_tempF)

# Creating a dataframe from scratch 

data_dict = {
  "students": ["Amy", "James", "Angela"],
  "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)

#convert dataframe to csv

data.to_csv("new_data.csv")