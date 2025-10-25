import turtle
import pandas

screen = turtle.Screen()
screen.title("Nigeria States Game")
image = "map_of_Nigeria.gif"
#screen.bgpic(image)

turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("37_states.csv")
state_list = data.state.to_list()
guessed_states = []





while len(guessed_states) < 37:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/37 States Correct", prompt="What's another state's name?").title()
    
    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
 
    if answer_state in state_list:
        guessed_states.append(answer_state)
        print(answer_state)
        state_data = data[data.state  == answer_state]
        x_cor = int(state_data.x.iloc[0])
        y_cor = int(state_data.y.iloc[0])
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x=x_cor, y=y_cor)
        t.write(answer_state)
        


        





