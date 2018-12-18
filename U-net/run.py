from model import *
from data import *

''' Here is the training code, if you want: training time with 16 CPUs and a GPU: ~25 hours
# data augmentation specifications
data_gen_args = dict(rotation_range=45,
                    width_shift_range=0.05,
                    height_shift_range=0.05,
                    shear_range=0.05,
                    zoom_range=0.05,
                    horizontal_flip=True,
                    fill_mode='reflect',
                    vertical_flip=True)

#training data
trainDataGen = trainGenerator(2,'data/roadsegmentation/train','image','label',data_gen_args,save_to_dir = None)

#model
model = unet()

#checkpoints, in case of midway crashes
model_checkpoint = ModelCheckpoint('unet_roads.hdf5', monitor='loss',verbose=1, save_best_only=True)

#train the model on the augmented data
model.fit_generator(trainDataGen,steps_per_epoch=2000,epochs=5,callbacks=[model_checkpoint])

'''

# load test data
testGene = testGenerator("data/roadsegmentation/test", 50, (608,608))

# get model with pretrained results
model = unet(pretrained_weights="unet_roads.hdf5", input_size = (608,608,3))

# predict results
results = model.predict_generator(testGene,50,verbose=1)

# save predicted images
saveResult("data/roadsegmentation/test/predictions",results)