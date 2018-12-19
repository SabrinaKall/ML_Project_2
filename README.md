# Project Road Segmentation

## Structure

Our project can be divided into three parts, each of which can be treated as an independant subproject. They all have a similar structure, with notebooks containing classifiers at the root that store predictions in a `predictions` folder, as well as a `mask_to_submission.py` file that transforms these predictions into a csv file, stored in the `submissions` folder

### Basic_Models

This folder contains a series of notebooks, using "traditional" (read, non-neural network) classifiers, including our initial baseline `Default_submission.ipynb`. They are numbered in order and each contain a decription within.

The folder also contains a `metrics`folder, which contains a notebook for analysis of the training data.

### Given_neural_network

This folder contains given neural network adapted as a python notebook `Given_NN.ipynb`, from the original code in the `tf_aerial_images.py` file. The rest of the set-up is identical to the `Basic_Models`folder.

### U-net

This folder contains the U-net classifier, composed of a training notebook `trainUnet.ipynb`and a testing notebook `testUnet.ipynb` (although the trainUnet-upynb is also equipped to create test predictions). The reason for this separation lies in the amount of time it takes to run the training, ranging from 5 to 15 hours per epoch depending on resources. The two notebooks are currently set up for our best results (color images with 45° rotation), but contain instructions to modify the parameters.

The model itself is stored in the `model.py`file and the functions to exploit it in the `data.py`file.

There is also the `dataAugmentationVisualisation.ipynb` notebook, which demonstrates in more detail how data augmentation is done.

As this is our best classifier, the `run.py`file is located here. It can be used according to the following instructions. Note that due to the extensive runtime of the best classifier, we are providing you with the final weights. But as these are stored in a file too large to submit, you first need to download it from Google Drive using the provided link.

### run.py instructions
