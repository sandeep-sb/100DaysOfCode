import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

text = turtle.Turtle()
text.hideturtle()
text.penup()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state "
                                                                                             "name?").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        x_cor = float(state_data.x)
        y_cor = float(state_data.y)

        text.goto(x=x_cor, y=y_cor)
        text.write(f"{answer_state}")

# Create missing_state.csv
missed_state = []
for state in all_states:
    if state not in guessed_states:
        missed_state.append(state)
missing_state = pandas.DataFrame(missed_state)
missing_state.to_csv("missing_state.csv")
