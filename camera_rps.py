
#TODO the order of your methods inside the script does not really matter, however it would be more readable and easier to understand for someone 
# that reads this code for the first time if they could see the methods ordered based on their order of execution.
#TODO follow the other TODO s added to your methods
#TODO maybe format the messages printed on the screen - they can start with a capital letter for example
#TODO reformat your code so you can get rid of blank lines and unwanted comments and also add some blank lines to improve readability - find example 
#in the play_game function 
#WELL DONE!!! Apart from these comments, the code looks really nice. 


#import libraries
import time
import numpy as np
import cv2
from keras.models import load_model
import random

# define RPS game as a class
class RPSgame:
    
    # class constructor
    def __init__(self):

        #TODO maybe rename the 'failed_to_get_user_move' variable with a more descriptive name? 
         
        self.move_lookup= {
                0 : "Rock",
                1 : "Paper",
                2 : "Scissors",
                3 : "Nothing"
                }
        self.user_wins=0
        self.model=load_model('keras_model.h5')
        self.computer_wins=0
        self.failed_to_get_user_move=0
        self.intermission=3 # number of seconds to show intermission screens
        self.font=cv2.FONT_HERSHEY_SIMPLEX
        self.fontcolor= (255, 255, 255)
        self.cap = cv2.VideoCapture(0)

    def stop_video(self):
        # After the loop release the self.cap object
        self.cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

    # Function to overlay the intro messages on the camera input
    def play_intro(self):

        introtime=3
        t_zero=time.time()
        
        while time.time() < t_zero+introtime:

            ret, frame = self.cap.read()
            overlaytext="LET'S PLAY ROCK, PAPER, SCISSORS."
            frame2=cv2.putText(frame, overlaytext, (50, 50), self.font, 1, self.fontcolor, 2, cv2.LINE_AA)
            overlaytext2="first to three wins!."
            frame2=cv2.putText(frame2, overlaytext2, (50, 100), self.font, 1, self.fontcolor, 2, cv2.LINE_AA)
            # Display the resulting frame
            cv2.imshow('frame', frame2)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.stop_video()
        

    # Function to aquire computer's move

    def get_computer_choice(self):
        move_list = ["Rock", "Paper", "Scissors"]
        # Choose a random word from the list of possible words
        self.computer_choice = random.choice(move_list)
        
    
    # Function to determine the winner of each game

    def get_winner(self):

        # options_lookup = {v: k for k, v in self.move_lookup[0:4]}
        if self.user_choice=="Nothing": # all the nothing plays
            print('invalid user choice')
            self.failed_to_get_user_move+=1
            
        else:
            options_lookup = {"Scissors": 0, "Paper": 1, "Rock": 2}
            self.computer_choice=options_lookup[self.computer_choice]
            self.user_choice=options_lookup[self.user_choice]
            
            if self.user_choice == self.computer_choice: 
                print("it's a draw!")
                

            elif (self.user_choice- self.computer_choice) % 3 == 1:
                print("computer wins!")
                self.computer_wins+=1
                
            else:
                print("user wins!")
                self.user_wins+=1
                

        
    # Function to determine the user's move from the camera input
    def get_prediction(self):

        # create np array to store model input
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        # timebase initialise
        time_init=time.time() 

        # countdown variable
        countmax=3

        # run a capture countdown
        while time.time() < time_init+countmax:
        
            # Capture the video frame
            # by frame
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = self.model.predict(data)
            cdowntext = str(int(time_init+countmax-time.time()))
            predicttext=self.move_lookup[prediction.argmax()]
            frame2=cv2.putText(frame, cdowntext, (50, 50), self.font, 1, self.fontcolor, 2, cv2.LINE_AA)
            frame2=cv2.putText(frame, predicttext, (100, 50), self.font, 1, self.fontcolor, 2, cv2.LINE_AA)
            # Display the resulting frame
            cv2.imshow('frame', frame2)
            #print(move_lookup[prediction.argmax()])

            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.stop_video()
    
        self.user_choice=self.move_lookup[prediction.argmax()]
        return()
    
    
    
    # Function to display any string contained in "msg1" and "msg2", overlaid on the camera feed.
    def user_update(self, msg1, msg2):
        t_zero=time.time()
        
        while time.time() < t_zero+self.intermission:
            ret, frame = self.cap.read()
            frame2=cv2.putText(frame, msg1, (50, 50), self.font, 1, self.fontcolor, 2, cv2.LINE_AA)
            frame2=cv2.putText(frame2, msg2, (50, 100), self.font, 1, self.fontcolor, 2, cv2.LINE_AA)
            # Display the resulting frame
            cv2.imshow('frame', frame2)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.stop_video()
        
        
        

def play_game(nwins):

    game=RPSgame()
    game.play_intro()
    
    while True:
        if game.user_wins==nwins:
            msg1="Player Wins " + str(nwins) +" games!"
            msg2="GAME OVER"
            game.user_update(msg1,msg2)
            game.stop.video()
            
        elif game.computer_wins==nwins:
            msg1="Computer Wins " + str(nwins) +" games!"
            msg2="GAME OVER"
            game.user_update(msg1,msg2)
            game.stop.video()

        elif game.failed_to_get_user_move==5:
            msg1="failed to get player move too many times!"
            msg2=" "
            game.user_update(msg1,msg2)
            game.stop.video()

        else:
            game.get_computer_choice()
            game.get_prediction()
            game.get_winner()

        msg1="computer wins: " + str(game.computer_wins)
        msg2="player wins: " + str(game.user_wins)
        game.user_update(msg1,msg2)
        
        
   
            
     


play_game(3)