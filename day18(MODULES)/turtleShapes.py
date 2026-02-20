from turtle import Turtle,Screen
# from random import randint


tim = Turtle()
tim.shape("turtle")
tim.color("DodgerBlue")
tim.speed(1)
color = []

#the function draw shapes has the parameter of num_sides which is the argument from the for loop
def draw_shape(num_sides):
    
    #num_sides is what is not constant in the equation
    angle = 360 / num_sides
    
    #create a for loop to loop through the number of sides.
    for _ in range(num_sides):
        tim.fd(100)
        tim.rt(angle)

 # create a for loop to loop 4 - 10 times
for shape_side_n in range(3,11):
    tim.color(random.choice(color))
    #use a function in a loop
    draw_shape(shape_side_n)
        
screen = Screen()
screen.exitonclick()

# import heroes
# print(heroes.gen())

# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("DodgerBlue")

# for _ in range(15):
#     timmy.fd(10)
#     timmy.pu()
#     timmy.fd(10)
#     timmy.pd()

# screen = Screen()
# screen.exitonclick()