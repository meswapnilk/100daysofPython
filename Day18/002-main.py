from turtle import Turtle, Screen

timy_the_turtle = Turtle()
# screen = Screen()

timy_the_turtle.shape("turtle")
timy_the_turtle.color("red")
# screen.exitonclick()

for _ in range(4):
    timy_the_turtle.forward(100.0)
    timy_the_turtle.left(90.0)
