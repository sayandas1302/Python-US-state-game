from pandas import *
from screen import *
from player_pen import *

# extract the state names from the states data
data = read_csv("50_states.csv")
state_name = data.state.to_list()

# setup the screen
screen = Screen()
screen_setup(screen)
image = "blank_states_img.gif"
shape(image)
is_game_on = True
guessed_state = []

# start the game and repeat it
while len(guessed_state) < 50:

    # ask for a guess of a state
    guess = screen.textinput(prompt = "Guess a state name", title = f"{len(guessed_state)}/50 states correct").title()

    # stop the game when the user inserts exit
    if guess == "Exit":
        break

    # for a correct guess include it in the guessed_state list and put the name on the map
    if guess in state_name and guess not in guessed_state:
        guessed_state.append(guess)
        state_data = data[data.state == guess]
        t = Pen(int(state_data.x), int(state_data.y), guess.title())
        
# single out all the states that are not guessed by the user and show then in a seperate csv file
missing_states = [state for state in state_name if state not in guessed_state]
new_data = DataFrame(missing_states)
new_data.to_csv("States_to_learn.csv")
screen.exitonclick()