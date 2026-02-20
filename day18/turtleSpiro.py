import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

tim.shape("turtle")
tim.speed("fastest")

#create a function to generate a random color and return the result color to the function call.
def rand_col():
    #selects a random integer
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    r_col = (r,g,b)
    return r_col
def draw_spiro(size_of_gap):
    #create a for loop to continue printing circles.
    for _ in range(int(360/size_of_gap)):
        #provide the radius and the color for the turtle
        tim.circle(100)
        tim.color(rand_col())
        
        #change the heading and the heading angle direction.
        c_heading = tim.heading()
        tim.setheading(c_heading + size_of_gap)

draw_spiro(100)
        
#this is here because code is read from top to bottom and it follows a exitonclick event.  
screen = t.Screen()
screen.exitonclick()