# import turtle,Screen

# timmy = turtle.Turtle()

# from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy  = Turtle()
# timmy.shape("turtle")
# timmy.color("DodgerBlue")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


#this is how to add a prettytable format to display 
# table = PrettyTable()
# print(table)
# table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# table.add_row(["Adelaide", 1295, 1158259, 600.5])
# table.add_row(["Brisbane", 5905, 1857594, 1146.4])
# table.add_row(["Darwin", 112, 120900, 1714.7])
# table.add_row(["Hobart", 1357, 205556, 619.5])
# table.add_row(["Sydney", 2058, 4336374, 1214.8])
# table.add_row(["Melbourne", 1566, 3806092, 646.9])
# table.add_row(["Perth", 5386, 1554769, 869.4])

# print(table)

pokemon = PrettyTable()
pokemon.field_names = ["Pokemon Name","Type"]
pokemon.add_row(["Pikachu", "Electric"])
pokemon.add_row(["Squirtle", "Water"])
pokemon.add_row(["Charmander", "Fire"])
print(pokemon)

table = PrettyTable()
table.add_column("Pokemon",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])


print(table.align) #center align
table.align = "l" #left align
print(table)zv