import random
from turtle import Turtle, Screen


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


angles = [0, 90, 180, 270]

emmanuel = Turtle()
emmanuel.shape('turtle')
emmanuel.color('violet')

screen = Screen()
screen.colormode(255)

for _ in range(4):
    emmanuel.forward(100)
    emmanuel.left(90)
for _ in range(4):
    emmanuel.backward(100)
    emmanuel.left(90)
for _ in range(4):
    emmanuel.forward(100)
    emmanuel.right(90)
for _ in range(4):
    emmanuel.backward(100)
    emmanuel.right(90)

for _ in range(15):
    emmanuel.forward(10)
    emmanuel.penup()
    emmanuel.forward(10)
    emmanuel.pendown()

for x in range(3, 10):
    emmanuel.color(random_colour())
    for i in range(x):
        emmanuel.forward(100)
        emmanuel.right(360 / x)

for x in range(200):
    emmanuel.pensize(10)
    emmanuel.speed(0)
    emmanuel.color(random_colour())
    emmanuel.setheading(random.choice(angles))
    emmanuel.forward(25)


def spirograph(deg):
    emmanuel.speed(0)
    for _ in range(int(360 / deg)):
        emmanuel.color(random_colour())
        emmanuel.circle(100)
        emmanuel.setheading(emmanuel.heading() + deg)


spirograph(2)

screen.exitonclick()
