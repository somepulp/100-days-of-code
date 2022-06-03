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

#data = pd.read_csv("./weather_data.csv")

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

# data_dict = {
#   "students": ["Amy", "James", "Angela"],
#   "scores": [76, 56, 65]
# }

# data = pd.DataFrame(data_dict)

# convert dataframe to csv

# data.to_csv("new_data.csv")

# Create table with fur colour and count

squirrel_data = pd.read_csv("./squirrel_data.csv")

counts = squirrel_data['Primary Fur Color'].value_counts().to_list()
fur_color = squirrel_data['Primary Fur Color'].value_counts().index.to_list()

new_data = {
  "Fur Colour": fur_color,
  "Count": counts
}

new_data_df = pd.DataFrame(new_data)
new_data_df.to_csv("squirrel_count.csv")

#Alternative method

gray_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

data_dict = {
  "Fur Color": ["Gray", "Cinnamon", 'Black'],
  "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

print(pd.DataFrame(data_dict))