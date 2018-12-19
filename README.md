# Project Road Segmentation

#### Structure

Our project can be divided into three parts, each of which can be treated as an independant subproject. They all have a similar structure, with notebooks containing classifiers at the root that store predictions in a `predictions` folder, as well as a `mask_to_submission.py` file that transforms these predictions into a csv file, stored in the `submissions` folder.

### Basic_Models

This folder tests various "basic" (read non-neural network) classifiers.
 
#### File distribution

##### Notebooks: see content for details
* __1\_Default\_submission.ipynb__: Baseline: logistic regression
* __2\_Default\_submission\_change\_regularisation.ipynb__
* __3_Patch_size_variation.pynb__
* __4\_Colour_submission.ipynb__
* __5\_Colour_image\_enhancement.ipynb__
* __5b\_adapteq\_clip\_limit.ipynb__
* __6\_K\_neighbours.ipynb__

##### Conversion files:
* __mask\_to\_submission.py__: converts predicted images into labels in csv file
* __submission\_to_mask.py__: reconverts csv labels to png images

##### Data

* __predictions__: contains the images predicted by a run classifier
* __submissions__: contains the predicted images' as csv files of labels (stored here by mask\_to\_submission.py)
* __test_set_images__: test images
* __training__: training images and their groundtruths

##### Other
* __metrics__: Folder containing notebooks to analyse provided training images




### Given_neural_network

This folder tests the neural network provided with the project

#### File distribution

* __Given_NN.ipynb__: Given neural network converted to notebook
* __tf_aerial_images.py__: Original given neural network
* __predictions__: contains the images predicted by a run classifier
* __submissions__: contains the predicted images' as csv files of labels (stored here by mask\_to\_submission.py)
* __test_set_images__: test images
* __training__: training images and their groundtruths
* __mask\_to\_submission.py__: converts predicted images into labels in csv file
 

### U-net

This folder contains the U-net classifier.


####File distribution
* __model.py__: 				functions related to model definition
* __data.py__: 				functions related to data augmentation
* __trainUnet.ipynb__: 			training the neural network
* __testUnet.ipynb__: 			predicting test labels
* __dataAugmentationVisualisation.ipynb__: 	examples of augmentations we are applying, and the reasoning behind them
* __mask\_to\_submission.py__:			converting labels in png to csv
* __graphs__: folder to create graphs of classifier performance
* __predictions__: contains the images predicted by a run classifier
* __submissions__: contains the predicted images' as csv files of labels (stored here by mask\_to\_submission.py)
* __data__: contains training and test data
* __run.py__: automated version of best submission




#### run.py instructions

0. If not yet done, install tensorflow version 1.12.0 (https://www.tensorflow.org/install/) and keras version 2.2.4 (https://keras.io/)
   If you have pip, you can use the following commands:
	pip install keras
	pip install tensorflow

1. Download the weights from the following link: https://drive.google.com/open?id=1cShMMg8ZWikr1rF692MBuR4HS1ON7NHL

2. Move the weights file to the directory `U-net/`
3. Run the run.py file to create predictions of the test images using the weights: `python3 run.py` 

The predicted images are now in the `predictions` folder and the labels in the `submissions/submission.csv` file.

