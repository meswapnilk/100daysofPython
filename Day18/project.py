import turtle as t
import random

tim = t.Turtle()
tim.speed("fast")
t.colormode(255)
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 101

for dot_count in range(1, number_of_dots):
    tim.color((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    tim.dot(20,((random.randint(0,255), random.randint(0,255), random.randint(0,255))))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()