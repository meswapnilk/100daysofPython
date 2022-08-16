import turtle as t
import random

tim = t.Turtle()

# tim.pensize(15)
tim.speed("fastest")
t.colormode(255)

for _ in range(180):
    tim.color((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    tim.circle(100)
    current_heading = tim.heading()
    tim.setheading(current_heading + 5)
