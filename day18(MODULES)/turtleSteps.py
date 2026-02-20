import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

tim.shape("turtle")
tim.speed("fastest")
tim.pensize(10)
directions = [0, 90, 180, 270]

#create a function to generate a random color.
def rand_col():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rand_col = (r,g,b)
    return rand_col

#take a walk in random direction with random color
for _ in range(300): 
    #call the function to retrieve a random color
    tim.color(rand_col())
    
    #use random.choice to retrieve a random direction
    tim.setheading(random.choice(directions))
    tim.fd(20)
        
#this is here because code is read from top to bottom and it follows a exitonclick event.  
screen = Screen()
screen.exitonclick()