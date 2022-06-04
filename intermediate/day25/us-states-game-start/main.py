import turtle
import pandas as pd 
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)


states_data = pd.read_csv("./50_states.csv")
states = states_data["state"].to_list()

num_correct = 0 


while num_correct < 50: 

    answer_state = screen.textinput(title=f"{str(num_correct)}/50 States Correct", 
                                    prompt="What's another state's name?").title()
    if answer_state in states: 
        num_correct += 1
        states.remove(answer_state)
        answer_turtle = turtle.Turtle()
        answer_turtle.hideturtle()
        answer_turtle.penup()
        answer_row = states_data[states_data.state == answer_state]
        answer_turtle.setpos(answer_row.x.item(), answer_row.y.item())
        answer_turtle.write(answer_state, move=True,font=('Arial', 6, 'normal'),align='Center')
    

screen.exitonclick()
