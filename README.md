# Computer Vision RPS

## Project Outline

This is a simple computer vision machine learning project, creating a simple game of rock-paper-scissors which can be played betweeen a human and computer player via the webcam interface. It is developed in Python, leveraging a Keras/Tensorflow model trained automatically with human input to a web based tool, Teachable-Machine (https://teachablemachine.withgoogle.com/faq).

## Milestones 1 and 2:

The initial model is a simple 4-state computer vision model, generated via Teachable Machine's web interface. The model is trained on webcam image input (n=500 /class) of four classes (Rock, Paper, Scissors, None), during which a single user presents the relevant game move to the webcam in a variety of locations and orientations. 

The model (using Keras API for Tensorflow) is then trained remotely on the web tool, and preview tested on the Teachable Machine web interface.

Preliminary qualitative testing indicates a passable discrimination between classes, with the model defaulting to the "nothing" class when no hand input was shown. There are noticeable edge cases, not least the literal edge case of some inputs being unidentifiable when presented at the edges of the FOV. Optimisation of the model itself should be revisited in a future milestone.

## Milestones 3 and 4:

As a precursor to the computer-vision version of the game, the file manual_rps.py contains a simple manual-play version of the game. This version consists of four functions:

- get_user_choice() - this function requests input from the user inside an iterative while loop, using a single keypress. If a valid keypress is made, it returns the relevant string (eg. "r" input gives "Rock) via a dictionary lookup, else it prompts the user for a valid keypress.

- get_computer_choice() - this function uses the choice method from the random package to make a random choice from the three possible moves, and returns the move.

- get_winner() - this function takes the outputs of get_user_choice() and get_computer_choice() and returns the game outcome. The game logic is coded in nested if loops.

- play() - a wrapper function that prompts describes the game workflow, prompting and informing the user with short time delays introduced by the time.sleep() method from the time package. It then updates the user with the result of the game. 

## Milestone 5

### Getting user input via Keras model

The function get_prediction() opens an openCV capture window and passes each capture frame to the input layer of the keras model. The captured frame is then displayed with a countdown timer in seconds and the current prediction of the model, for user feedback. When the countdown timer reaches zero, the move corresponding to the argmax of the softmax layer on that frame is returned as an output of the function.

### Making the full game

The functions get_prediciton(), get_computer_choice() and get_winner() are wrapped as methods of a class, RPS. The init method of the class requires the keras model as an input, and assigns number of wins for each player as attributes.

The final game is then created using a function, play_game(), which creates an instance of RPS, and runs repeat instances of the game by calling its methods inside an iterating while loop, which terminates if either player reaches three wins.