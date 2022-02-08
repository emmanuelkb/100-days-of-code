from turtle import Turtle, Screen
import random

color_list = [(202, 164, 110), (149, 75, 50),
              (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129),
              (147, 17, 19), (27, 68, 102),
              (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]

emmanuel = Turtle()
screen = Screen()
screen.colormode(255)
emmanuel.shape('arrow')

x=10
for _ in range(8):
    emmanuel.home()
    emmanuel.sety(x)
    for _ in range(10):
        emmanuel.pendown()
        emmanuel.dot(20, random.choice(color_list))
        emmanuel.penup()
        emmanuel.forward(50)
        x+=5
    if _ == 9:
        emmanuel.hideturtle()

screen.exitonclick()
