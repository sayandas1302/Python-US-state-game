FONT = ("arial", 10, "normal")
from turtle import *
class Pen(Turtle):
    def __init__(self, x , y, Name):
        '''all the set for the turtle writing the state name on the blank map'''
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(Name, align = "center", font = FONT)