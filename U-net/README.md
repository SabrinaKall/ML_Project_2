# Best submission recreation

Note that we simply provide the trained weights of our best model, as creating these took close to 25 hours.

## Instructions for recreating the predictions

0. If not yet done, install tensorflow version 1.12.0 (https://www.tensorflow.org/install/) and keras version 2.2.4 (https://keras.io/)
   If you have pip, you can use the following commands:
	pip install keras
	pip install tensorflow

1. Download the weights from the following link: https://drive.google.com/open?id=1cShMMg8ZWikr1rF692MBuR4HS1ON7NHL

2. Move the weights file to the directory `U-net/`
3. Run the run.py file to create predictions of the test images using the weights: `python3 run.py` 

The predicted images are now in the `data/roadsegmentation/test/predictions` folder and the labels in the `data/roadsegmentation/submission.csv` file.

## File distribution
model.py: 				functions related to model definition
data.py: 				functions related to data augmentation
trainUnet.ipynb: 			training the neural network
testUnet.ipynb: 			predicting test labels
dataAugmentationVisualisation.ipynb: 	examples of augmentations we are applying, and the reasoning behind them
mask_to_submission.py:			converting labels in png to csv
