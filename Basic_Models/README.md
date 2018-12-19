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