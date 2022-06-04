import turtle
import pandas as pd 
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)


states_data = pd.read_csv("./50_states.csv")
states = states_data["state"].to_list()

screen.exitonclick()
