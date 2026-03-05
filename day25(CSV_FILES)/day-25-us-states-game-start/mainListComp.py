import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States")
#image must be saved as a gif before implemented in screen.addshape()
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./50_states.csv")
all_states = data.state.to_list()
guess_states = [] 

while len(guess_states) < 50:
    ans_state = screen.textinput(title = f"{len(guess_states)}", prompt="Whats another state name?").title()
    print(ans_state)    
    if ans_state == "exit":
        break 
    # miss_states = []                  {var_name}
    # for state in all_states:          {for- loop}
    #     if state not in guess_state:  {condition}
    #         miss_states.append(state) {expression}
    #using list comprehension learnt in day26
    miss_state = [state for state in all_states if state not in guess_states]
    new_data = pandas.DataFrame(miss_states)
    new_data.to_csv("states_to_learn.csv")
         
    if ans_state in all_states:
        guess_states.append(ans_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == ans_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())


screen.exitonclick()