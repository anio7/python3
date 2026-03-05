from turtle import Turtle, Screen
import pandas

turtle = Turtle()
screen = Screen()

screen.title("U.S States...game")

#image must be saved before implemented
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


ans_state = screen.textinput(title = "Guess the state", prompt="Whats another state name?").title()
print(ans_state)

us50_states = pandas.read_csv("./50_states.csv")
# us50_states[us50_states[]]

user_guess = True
while user_guess:
    pass