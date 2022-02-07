import random
from turtle import Turtle, Screen

colours = ['Dark Red', 'Dark Blue', 'Aquamarine', 'Dark Green', 'Red', 'Purple','Orchid','Maroon']
angles = [0,90,180,270]

emmanuel = Turtle()
emmanuel.shape('turtle')
emmanuel.color('violet')

# for _ in range(4):
#     emmanuel.forward(100)
#     emmanuel.left(90)
# for _ in range(4):
#     emmanuel.backward(100)
#     emmanuel.left(90)
# for _ in range(4):
#     emmanuel.forward(100)
#     emmanuel.right(90)
# for _ in range(4):
#     emmanuel.backward(100)
#     emmanuel.right(90)

# for _ in range(15):
#     emmanuel.forward(10)
#     emmanuel.penup()
#     emmanuel.forward(10)
#     emmanuel.pendown()
#
# for x in range(3,13):
#     emmanuel.color(random.choice(colours))
#     for i in range(x):
#         emmanuel.forward(100)
#         emmanuel.right(360 / x)

for x in range(200):
    emmanuel.pensize(10)
    emmanuel.speed(0)
    emmanuel.color(random.choice(colours))
    emmanuel.setheading(random.choice(angles))
    emmanuel.forward(25)

screen = Screen()
screen.exitonclick()

