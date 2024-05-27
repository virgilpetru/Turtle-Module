import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.hideturtle()
color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
(138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
(232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89),
(82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

def turn_left():
    tim.left(90)
    tim.forward(50)
    tim.dot(20, random.choice(color_list))
    tim.left(90)
def turn_right():
    tim.right(90)
    tim.forward(50)
    tim.dot(20, random.choice(color_list))
    tim.right(90)
def draw_square():
    for _ in range(10):
        tim.penup()
        tim.forward(50)
        tim.dot(20, random.choice(color_list))
        tim.pencolor(random.choice(color_list))

def draw_square2():
    for _ in range(9):
        tim.penup()
        tim.forward(50)
        tim.dot(20, random.choice(color_list))
        tim.pencolor(random.choice(color_list))

draw_square()

for _ in range(10):
    turn_left()
    draw_square2()
    turn_right()
    draw_square2()

screen = turtle_module.Screen()
screen.exitonclick()
