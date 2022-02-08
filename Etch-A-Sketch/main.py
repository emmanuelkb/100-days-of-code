import turtle
from turtle import Turtle, Screen
import random

emmanuel = Turtle()
screen = Screen()
screen.colormode(255)
emmanuel.shape('arrow')
emmanuel.color('black')


def move_forward():
    emmanuel.forward(10)

def move_backward():
    emmanuel.backward(10)

def turn_left():
    emmanuel.setheading(emmanuel.heading()+10)

def turn_right():
    emmanuel.setheading(emmanuel.heading()-10)

def clear():
    emmanuel.clear()

screen.listen()
turtle.onkey(fun=move_forward,key='d')
turtle.onkey(fun=move_backward,key='a')
turtle.onkey(fun=turn_left,key='w')
turtle.onkey(fun=turn_right,key='s')
turtle.onkey(fun=clear,key='c')


screen.exitonclick()
