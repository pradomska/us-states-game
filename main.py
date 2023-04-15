import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
states_list = data["state"].to_list()
print(states_list)
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct", "What's another state's name?").title()
    print(answer_state)

    if answer_state in states_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto((int(state_data.x), int(state_data.y)))
        t.write(state_data.state.item())

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
