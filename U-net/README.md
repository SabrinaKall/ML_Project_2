# Best submission recreation

Note that we simply provide the trained weights of our best model, as creating these took close to 25 hours.

## Instructions

0. If not yet done, install tensorflow (https://www.tensorflow.org/install/)

1. Download the weights from the following link: https://drive.google.com/open?id=1cShMMg8ZWikr1rF692MBuR4HS1ON7NHL

2. Move  the weights file to the directory `U-net/`
3. Run the run.py file to create predictions of the test images using the weights: `python3 run.py` 
4. run the mask\_to\_submission file to get the labels from the predicted images: `python3 mask_to_submission.py`

The labels are now in the `data/roadsegmentation/submission.csv`file.