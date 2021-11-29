from turtle import Turtle
import pandas


class State:
    def __init__(self, file):
        self.score = 0
        self.data = pandas.read_csv(file)
        self.all_states = self.data.state.tolist()

    def is_state_exist(self, answer):
        if answer in self.all_states:
            return True
        return False

    def get_state_position(self, answer):
        state = self.data[self.data.state == answer]
        x_val = int(state.x)
        y_val = int(state.y)
        position = (x_val, y_val)
        return position

    def print_state(self, position, answer):
        timmy = Turtle()
        timmy.penup()
        timmy.hideturtle()
        timmy.goto(position)
        timmy.write(answer)

    def score_up(self):
        self.score += 1
