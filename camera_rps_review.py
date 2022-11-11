#TODO the model variable has been created outside the class. 
# You can also create it as a static class variable - inside the class but outside the constructor (the __init__ method) or inside the constructor.
# Would be interseting to look at these 3 use cases and understand the differences
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

    # Function to aquire computer's move
    def get_computer_choice(self):
        # Define list of possible moves
        move_list = ["Rock", "Paper", "Scissors"]
        # Choose a random word from the list of possible words
        self.computer_choice = random.choice(move_list)
        return()
    
    # Function to determine the winner of each game
    def get_winner(self):
        # options_lookup = {v: k for k, v in self.move_lookup[0:4]}
        if self.user_choice=="Nothing": # all the nothing plays
            print('invalid user choice')
            self.failed_to_get_user_move+=1
            return()
        else:
            options_lookup = {"Scissors": 0, "Paper": 1, "Rock": 2}
            self.computer_choice=options_lookup[self.computer_choice]
            self.user_choice=options_lookup[self.user_choice]
            
            if self.user_choice == self.computer_choice: # all the equal plays
                print("it's a draw!")
                return()
            elif (self.user_choice- self.computer_choice) % 3 == 1:
                print("computer wins!")
                self.computer_wins+=1
                return()
            else:
                print("user wins!")
                self.user_wins+=1
                return()

        
    # Function to determine the user's move from the camera input
    def get_prediction(self):
        # define a video capture object
        cap = cv2.VideoCapture(0)
        # create np array to store model input
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        # timebase initialise
        time_init=time.time() 

        # move_lookup= {
        #     0 : "Rock",
        #     1 : "Paper",
        #     2 : "Scissors",
        #     3 : "Nothing"
        #     }

        # countdown variable
        countmax=3

        # run a capture countdown
        while time.time() < time_init+countmax:
        
            # Capture the video frame
            # by frame
            ret, frame = cap.read()
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

            # the 'q' button is set as the
            # quitting button you may use any
            # desired button of your choice
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
    #TODO you can create a separate method to stop the video, the code will look nicer and yur method won't be that big plus you avoid repeating code 
    #TODO you can aslo call the method at the end of your play_intro() and user_update() methods
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        self.user_choice=self.move_lookup[prediction.argmax()]
        return()
    
    # Function to overlay the intro messages on the camera input
    def play_intro(self):
        introtime=3
        cap = cv2.VideoCapture(0)
        t_zero=time.time()
        
        while time.time() < t_zero+introtime:
            ret, frame = cap.read()
            overlaytext="LET'S PLAY ROCK, PAPER, SCISSORS."
            frame2=cv2.putText(frame, overlaytext, (50, 50), self.font, 1, self.fontcolor, 2, cv2.LINE_AA)
            overlaytext2="first to three wins!."
            frame2=cv2.putText(frame2, overlaytext2, (50, 100), self.font, 1, self.fontcolor, 2, cv2.LINE_AA)
            # Display the resulting frame
            cv2.imshow('frame', frame2)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
    
    # Function to display any string contained in "msg1" and "msg2", overlaid on the camera feed.
    def user_update(self, msg1, msg2):
        #TODO overlaytext2 is not being used after initialised. Solve this :)
        cap = cv2.VideoCapture(0)
        t_zero=time.time()
        
        while time.time() < t_zero+self.intermission:
            ret, frame = cap.read()
            frame2=cv2.putText(frame, msg1, (50, 50), self.font, 1, self.fontcolor, 2, cv2.LINE_AA)
            overlaytext2="first to three wins!."
            frame2=cv2.putText(frame2, msg2, (50, 100), self.font, 1, self.fontcolor, 2, cv2.LINE_AA)
            # Display the resulting frame
            cv2.imshow('frame', frame2)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        
    

        


def play_game(nwins):
    #TODO remove blank line 
    #TODO remove blank line 
    game=RPSgame()
    # print("Let's play Rock, Paper, Scissors - First to 3 wins!")
    game.play_intro()
    
    while True:
        if game.user_wins==nwins:
            #TODO remove blank line 
            msg1="Player Wins " + str(nwins) +" games!"
            msg2="GAME OVER"
            game.user_update(msg1,msg2)
            
        elif game.computer_wins==nwins:
            msg1="Computer Wins " + str(nwins) +" games!"
            msg2="GAME OVER"
            game.user_update(msg1,msg2)
            return()
        #TODO blank line here
        elif game.failed_to_get_user_move==nwins:
            msg1="failed to get player move too many times!"
            msg2=" "
            game.user_update(msg1,msg2)
            return()
        #TODO blank line here
        else:
            game.get_computer_choice()
            game.get_prediction()
            game.get_winner()
        #TODO blank line here
        msg1="computer wins: " + str(game.computer_wins)
        msg2="player wins: " + str(game.user_wins)
        game.user_update(msg1,msg2)
        # print("computer wins: " + str(game.computer_wins))
        # print("player wins: " + str(game.user_wins)) 
        
   
            
     


play_game(3)