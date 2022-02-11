from turtle import Screen, Turtle
import pandas
screen = Screen()
turtle = Turtle()
name = "blank_states_img.gif"

screen.addshape(name)
turtle.shape(name)

screen.title('US States Game')

data = pandas.read_csv("50_states.csv")
states = data.state.tolist()
states = [x.lower() for x in states]
x_cor = data.x.tolist()
y_cor = data.y.tolist()

a = data.to_dict()
print(a)

# for state in range(len(states)):
#     guess = screen.textinput("Which State?", "Type a state")
#     if guess.lower() in states:
#         turtle.setposition(x_cor, y_cor)
#         turtle.write(guess, align="right")
#
# screen.mainloop()