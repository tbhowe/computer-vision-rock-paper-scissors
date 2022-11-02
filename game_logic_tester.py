# This short script defines the simple game logic of Rock, Paper, Scissors

#If computer plays ROCK

    # if player plays ROCK
    # elif player plays PAPER
    # elif player plays SCISSORS

# elif computer plays PAPER

    # if player plays ROCK
    # elif player plays PAPER
    # elif player plays SCISSORS

# elif computer plays SCISSORS

    # if player plays ROCK
    # elif player plays PAPER
    # elif player plays SCISSORS

computer_move='Paper'
user_move='Rock'

if computer_move=='Rock':

    if user_move=='Rock':
        print("it's a draw!")
    elif user_move=='Paper':
        print("user wins! (Paper wraps Rock)")
    elif user_move=='Scissors':
        print("user loses! (Rock blunts Scissors)")

elif computer_move=='Paper':

    if user_move=='Rock':
        print("user loses! (Paper wraps Rock)")
    elif user_move=='Paper':
        print("it's a draw!")
    elif user_move=='Scissors':
        print("user wins! (Scissors cut Paper)")  

elif computer_move=='Scissors':
    if user_move=='Rock':
        print("user wins! (Rock blunts Scissors)")
    elif user_move=='Paper':
        print("user loses! (Scissors cut Paper)")
    elif user_move=='Scissors':
        print("it's a draw!")