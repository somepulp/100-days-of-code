# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('Seagreen4')

# my_screen = Screen()
# print(timmy.position())
# timmy.forward(100)
# print(timmy.position())

# my_screen.exitonclick()

from prettytable import PrettyTable
from prettytable.prettytable import DOUBLE_BORDER

table = PrettyTable()
table.set_style(DOUBLE_BORDER)
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)