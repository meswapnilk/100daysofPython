from turtle import Turtle
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tim = Turtle()

for i in range(3,11):
    tim.color(random.choice(colours))
    for _ in range(i):
        tim.forward(100.0)
        tim.right(360/i)