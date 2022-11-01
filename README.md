# Computer Vision RPS

This is a simple computer vision machine learning project, creating a simple game of rock-paper-scissors which can be played betweeen a human and computer player via the webcam interface. It is developed in Python, leveraging a Keras/Tensorflow model trained automatically with human input to a web based tool, Teachable-Machine (https://teachablemachine.withgoogle.com/faq).

Milestone 1-2:

The initial model is a simple 4-state computer vision model, generated via Teachable Machine's web interface. The model is trained on webcam image input (n=500 /class) of four classes (Rock, Paper, Scissors, None), during which a single user presents the relevant game move to the webcam in a variety of locations and orientations. 

The model (Keras API for Tensorflow) is then trained remotely on the web tool, and preview tested on the Teachable Machine web interface. Preliminary qualitative testing indicates a passable discrimination between classes, with the model defaulting to the "nothing" class when no hand input was shown. However there are noticeable edge cases, not least the literal edge case of some inputs being unidentifiable when presented at the edges of the screen. Optimisation of the model itself should be revisited in a future milestone.

