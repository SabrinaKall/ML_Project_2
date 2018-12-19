# Project Road Segmentation

## Structure

Our project can be divided into three parts, each of which can be treated as an independant subproject.

### Basic_Models

This folder contains a series of notebooks, using "traditional" (read, non-neural network) classifiers, including our initial baseline (`Default_submission.ipynb`). They are numbered in order and each contain a decription within. Each can be run separately to create a series of predicted images, stored in the `predictions` folder, which can be converted to a submission by running the `mask\_to\_submission.py` file. The submission will be saved in the `submissions` folder.

### Given_neural_network

This folder contains given neural network adapted as a python notebook.

### U-net

This folder contains the U-net classifier, composed of a training notebook (`trainUnet.ipynb`) and a testing notebook (`testUnet.ipynb`). To 
