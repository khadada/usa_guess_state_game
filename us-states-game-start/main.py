import turtle
import pandas
data = pandas.read_csv('50_states.csv')
all_states = data.state.tolist()
screen = turtle.Screen()
timmy = turtle.Turtle()
timmy.penup()
timmy.hideturtle()
screen.title('US States Games')
img = 'blank_states_img.gif'
screen.addshape(img)
turtle.shape(img)
score = 0
while True:
    answer = screen.textinput(title=f'score {score}/{len(all_states)}',prompt="What's the state: ").title()
    if answer in all_states:
        state = data[data.state == answer]
        x_value = int(state.x)
        y_value = int(state.y)
        print(f"x: {x_value}  y:{y_value}")
        timmy.goto(x_value, y_value)
        timmy.write(answer, align='center', font=('Courier', 6, 'bold'))
        score += 1
turtle.mainloop()

