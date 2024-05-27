import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tim.shape("turtle")
tim.pensize(width=2)
tim.speed(0)

for _ in range(36):
    tim.color(random_color())
    tim.circle(160, 360)
    tim.tilt(30)
    tim.right(20)
    tim.tilt(30)
    tim.left(10)
    tim.forward(1)

screen = t.Screen()
screen.exitonclick()


