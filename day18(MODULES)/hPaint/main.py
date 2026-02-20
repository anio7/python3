#to import colorgram you have install it first using - pip install colorgram.py
import random,turtle as t,colorgram as cg


colors = cg.extract("image.jpeg",60)
rgb_colors = []

#create a for loop for the colors and append it to a list:
for color in colors:   
    #retract each color using colorgram 
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    
    #create a tuple to be appended to the list.
    new_color = (r,g,b)
    rgb_colors.append(new_color)

#create turtle object variables.
tim = t.Turtle()
t.colormode(255)
tim.pensize(5)
tim.speed("fastest")
tim.shape("turtle")

#position turtle to the top of the page
tim.teleport(-460,-430)

#create a loop using turtle to print dots
def move_t():
    
    for _ in range(23):
        rand_col = random.choice(rgb_colors)
        tim.dot(20,rand_col)
        tim.pu()
        tim.fd(40)
        

move_t()
tim.lt(90)
tim.fd(40)
tim.lt(90)
move_t()
tim.rt(90)
tim.fd(40)
tim.rt(90)
move_t()

screen = t.Screen()
screen.exitonclick()