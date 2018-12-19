# Project Road Segmentation

#### Structure

Our project can be divided into three parts, each of which can be treated as an independant subproject. They all have a similar structure, with notebooks containing classifiers at the root that store predictions in a `predictions` folder, as well as a `mask_to_submission.py` file that transforms these predictions into a csv file, stored in the `submissions` folder

### Basic_Models

This folder contains a series of notebooks, using "traditional" (read, non-neural network) classifiers, including our initial baseline `Default_submission.ipynb`. They are numbered in order and each contain a decription within.

The folder also contains a `metrics`folder, which contains a notebook for analysis of the training data.

### Given_neural_network

This folder contains given neural network adapted as a python notebook `Given_NN.ipynb`, from the original code in the `tf_aerial_images.py` file. The rest of the set-up is identical to the `Basic_Models`folder.

### U-net

This folder contains the U-net classifier.


####File distribution
__model.py__: 				functions related to model definition
__data.py__: 				functions related to data augmentation
__trainUnet.ipynb__: 			training the neural network
__testUnet.ipynb__: 			predicting test labels
__dataAugmentationVisualisation.ipynb__: 	examples of augmentations we are applying, and the reasoning behind them
__mask\_to\_submission.py__:			converting labels in png to csv




#### run.py instructions

0. If not yet done, install tensorflow version 1.12.0 (https://www.tensorflow.org/install/) and keras version 2.2.4 (https://keras.io/)
   If you have pip, you can use the following commands:
	pip install keras
	pip install tensorflow

1. Download the weights from the following link: https://drive.google.com/open?id=1cShMMg8ZWikr1rF692MBuR4HS1ON7NHL

2. Move the weights file to the directory `U-net/`
3. Run the run.py file to create predictions of the test images using the weights: `python3 run.py` 

The predicted images are now in the `predictions` folder and the labels in the `submissions/submission.csv` file.

