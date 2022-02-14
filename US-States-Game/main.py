import turtle
import pandas

screen = turtle.Screen()
screen.title('US States Game')
name = "blank_states_img.gif"
screen.addshape(name)
turtle.shape(name)

data = pandas.read_csv("50_states.csv")
states = data.state.tolist()
states = [x.lower() for x in states]

guessed_states = []

while len(guessed_states) < 50:
    guess = screen.textinput(f"{len(guessed_states)}/50 States Correct",
                             "Type a state")
    if guess.lower() in states:
        t1 = turtle.Turtle()
        guessed_states.append(guess)
        t1.hideturtle()
        t1.penup()
        state_info = data[data['state'].str.lower() == guess.lower()]
        t1.goto(int(state_info.x), int(state_info.y))
        t1.write(guess)
    if guess.lower() == "exit":
        break
