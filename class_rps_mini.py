#import libraries
import time
import numpy as np
import cv2
from keras.models import load_model
import random

# load keras model for RPS
model = load_model('keras_model.h5')

class RPSgame:
    
    def __init__(self):
        self.move_lookup= {
                0 : "Rock",
                1 : "Paper",
                2 : "Scissors",
                3 : "Nothing"
                }
        self.user_wins=0
        self.computer_wins=0
        self.computer_choice = "Nothing"
        self.user_choice= "Rock"
        self.model=model
    
    def get_computer_choice(self):
        # Define list of possible moves
        move_list = ["Rock", "Paper", "Scissors"]
        # Choose a random word from the list of possible words
        self.computer_choice = random.choice(move_list)
        return()
    
    def get_winner(self):
        
        if self.computer_choice=='Rock':

            if self.user_choice=='Rock':
                print("it's a draw!")
                return()
            elif self.user_choice=='Paper':
                print("player wins! (Paper wraps Rock)")
                self.user_wins+=1
                return()
            elif self.user_choice=='Scissors':
                print("computer wins! (Rock blunts Scissors)")
                self.computer_wins+=1
                return()


        elif self.computer_choice=='Paper':

            if self.user_choice=='Rock':
                print("user loses! (Paper wraps Rock)")
                self.computer_wins+=1
            elif self.user_choice=='Paper':
                print("it's a draw!")
                return()
            elif self.user_choice=='Scissors':
                print("user wins! (Scissors cut Paper)") 
                self.user_wins+=1 
                return()

        elif self.computer_choice=='Scissors':
            if self.user_choice=='Rock':
                print("user wins! (Rock blunts Scissors)")
                self.user_wins+=1
                return()
            elif self.user_choice=='Paper':
                print("user loses! (Scissors cut Paper)")
                self.computer_wins+=1
                return()
            elif self.user_choice=='Scissors':
                print("it's a draw!")
                return()

game=RPSgame()
while True:
            if game.user_wins==3:
                print("Player Wins 3 games!")
                break
            elif game.computer_wins==3:
                print("Computer Wins 3 games!")
                break
            else:
                game.get_computer_choice()
                game.get_winner()
