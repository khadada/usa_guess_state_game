import turtle
from state_write import State
screen = turtle.Screen()
screen.title('US States Games')
img = 'blank_states_img.gif'
screen.addshape(img)
turtle.shape(img)
state = State('50_states.csv')
while True:
    answer = screen.textinput(title=f'score {state.score}/{len(state.all_states)}', prompt="What's the state: ").title()
    if state.is_state_exist(answer):
        position = state.get_state_position(answer)
        state.print_state(position, answer)
        state.score_up()
