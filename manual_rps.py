# Manual-only Rock-Paper-Scissors game


# import packages
import numpy as np
import random
# import cv2
# from keras.models import load_model

# Define the functions 

def get_computer_choice():
    # Define list of possible moves
    move_list = ["Rock", "Paper", "Scissors"]
    # Choose a random word from the list of possible words
    computer_choice = random.choice(move_list)
    return(computer_choice)

def get_user_choice():
    move_list = {
    "r": "Rock",
    "p": "Paper",
    "s": "Scissors"
    }
    while True:
        # Request input from user of a single letter
        user_choice=input("please enter a move (r,p,s = rock, paper, scissors")
        #checks that input is alphabetical AND of length 1. Escapes if both conditions met
        if user_choice in move_list.keys():
            print('thanks!')
            user_guess=move_list[user_choice]
            return(user_guess)
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

def get_winner(computer_choice,user_choice):
    if computer_choice=='Rock':

        if user_choice=='Rock':
            print("it's a draw!")
        elif user_choice=='Paper':
            print("user wins! (Paper wraps Rock)")
        elif user_choice=='Scissors':
            print("user loses! (Rock blunts Scissors)")

    elif computer_choice=='Paper':

        if user_choice=='Rock':
            print("user loses! (Paper wraps Rock)")
        elif user_choice=='Paper':
            print("it's a draw!")
        elif user_choice=='Scissors':
            print("user wins! (Scissors cut Paper)")  

    elif computer_choice=='Scissors':
        if user_choice=='Rock':
            print("user wins! (Rock blunts Scissors)")
        elif user_choice=='Paper':
            print("user loses! (Scissors cut Paper)")
        elif user_choice=='Scissors':
            print("it's a draw!")

# test the code
computer_choice=get_computer_choice()
print("computer's move is:")
print(computer_choice)

user_choice=get_user_choice()
print("user's move is:")
print(user_choice)

get_winner(computer_choice,user_choice)