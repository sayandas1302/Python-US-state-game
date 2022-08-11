from turtle import *

def screen_setup(screen):
    '''all the initial setup for the screen'''
    screen.title("The U.S State Game")
    screen.setup(725, 491)
    image = "blank_states_img.gif"
    screen.addshape(image)