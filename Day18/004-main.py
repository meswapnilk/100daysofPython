import turtle
from turtle import Turtle
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions= [0, 90, 180, 270]
tim = Turtle()
tim.pensize(15)
tim.speed("fastest")
turtle.colormode(255)
for _ in range(500):
    tim.color((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    tim.color()
    tim.setheading(random.choice(directions))
    tim.forward(50)

