"""
Training tf.keras files for the project

massive human and champanzee photos are used over this training model


Copyright by Wing Cheong Lo (c), 2019

trainingModel.py -- train an AI and store it in defined dir
"""
print(
"""
ACKNOWLEDGE
===========
 This project is created by Wing Cheong Lo, July 2019, on his cs003c course under
	the supervision of professor Jamal Ashref. This project aims to distinguish
	a photo containg a humanoid object and make a decision of whether the
	object is a human or a champanzee/monkey. 

	Limited by the skill of the creator, this project may not be highly accurate 
	and can only distinguish a human and champanzee. 

 This project is honored to use datasets from the following organization
        and as a requirement of the dataset provider, this program will make citations.
  
        All dataset provider have stated that the dataset 
		SHOULD NOT BE commerical uses and
	    should only be used on research or education.
  
	

CITATION
==========
 	humanSelfieDataSet -- University of Central Florida {
				@inproceedings{kalayeh2015selfie,
  				title={How to Take a Good Selfie?},
 			        author={Kalayeh, Mahdi M and Seifu, Misrak and LaLanne, Wesna and Shah, Mubarak},
  				booktitle={Proceedings of the 23rd Annual ACM Conference on Multimedia Conference},
 				pages={923--926},
  				year={2015},
  				organization={ACM}
				}
			       (3226 Images from total 47000 human selfies)
	

	
	champanzeeDataSet -- Alexander Freytag and Erik Rodner and Marcel Simon and Alexander Loos and Hjalmar Kühl 
			    "Chimpanzee Faces in the Wild: Log-Euclidean CNNs for Predicting Identities and Attributes of Primates"**, 
				    German Conference on Pattern Recognition (GCPR), 2016 .

			       (contribute approximately 1800 images for the monkey images in C Tai file)
			



                      -- kaggle and wikipedia open source
			    Content from the download page:
					The dataset consists of two files, training and validation.
					Each folder contains 10 subforders labeled as n0~n9, 
					each corresponding a species form Wikipedia's monkey cladogram. 
					Images are 400x300 px or larger and JPEG format (almost 1400 images).
					Images were downloaded with help of the googliser open source code.
					https://www.kaggle.com/slothkong/10-monkey-species

					(contribute approximately 1400 images for the 10 speices of monkey with different poses and color)
""")

import numpy as np

from tqdm import tqdm


import os

# Path for the champanzee data set directory
champanzeeDataSetDir_PATH = os.path.join("/home/kiroslo/machineLearning/FINALPROJECT--CS003C/training_data_set/champanzeeDataset")

# Path for the human selfie data set directory
humanselfieDataSetDir_PATH = os.path.join("/home/kiroslo/machineLearning/FINALPROJECT--CS003C/training_data_set/humanSelfieDataSet")

# Making a list with no.Of Images in the directory
champanzeeImages = os.listdir(champanzeeDataSetDir_PATH)

# Printing the number of champanzee photo in the directory
print ("===================================================\n\nThere are totally", \
    (len(champanzeeImages)) , "Images in the chmapanzee directory")

# Making a list with no.Of Images in the directory
humanImages = os.listdir(humanselfieDataSetDir_PATH)		# Printing the number of human photo in the directory
print("There are totally", (len(humanImages)), "Images in the human directory\n\n===================================================")

# Path for validation data for champanzee
champanzee_VALIDATION_DataSetDir_PATH = os.path.join(
"/home/kiroslo/machineLearning/FINALPROJECT--CS003C/validation_data_set/monkey")
champanzee_Validation_Images = os.listdir(champanzee_VALIDATION_DataSetDir_PATH)

# Path for validation data for human
humanselfie_VALIDATION_DataSetDir_PATH = os.path.join(
	"/home/kiroslo/machineLearning/FINALPROJECT--CS003C/validation_data_set/human")
human_Validation_Images = os.listdir(humanselfie_VALIDATION_DataSetDir_PATH)

import tensorflow as tf

class trainedModel:
	# tk.keras.models.Sequential -- making it as a sequential
	model = tf.keras.models.Sequential([

	# Note the input shape of all images are 300 x 300 x 3 bytes
	# Input layer
	# kernel size  : 32
	# fiter size   : 3x3
	# activation   : 'relu'
	# input_shpae  : 300 x 300 pixels with 3 bytes color
	# pooing layer : 2x2
	tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(300, 300, 3)),
	tf.keras.layers.MaxPooling2D(2, 2),


	# first convolutional layer
	# kernel size : 32
	# fiter size  : 3x3
	# activation  : 'relu'
	# pooing layer : 2x2
	tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
	tf.keras.layers.MaxPooling2D(2,2),

	# flatten the layers to be 2D matrix
	tf.keras.layers.Flatten(),


	# first neutron network hidden layer
	# number of neurons : 256
	# activation  : 'relu'
	tf.keras.layers.Dense(256, activation='relu'),

	# first neutron network hidden layer
	# number of neurons : 256
	# activation  : 'relu'
	tf.keras.layers.Dense(256, activation='relu'),

	# first neutron network hidden layer
	# number of neurons : 256
	# activation  : 'relu'
	tf.keras.layers.Dense(256, activation='relu'),

	#Sigmoid is used for two class while softmax is used for multipule class
	# The main reason why to use sigmoid function is because it exists between (0 to 1).
	# Therefore, it is especially used for models where we have to predict the probability as an output.
	# Since probability of anything exists only between the range of 0 and 1, sigmoid is the right choice.
	tf.keras.layers.Dense(1, activation='sigmoid')
])

# print a report for the model
model.summary()

from tensorflow.keras.optimizers import SGD
Optimizer = SGD(lr=1e-3, momentum=0.3, decay=0, nesterov=False)

# comparison of two class
model.compile(loss='binary_crossentropy',

			# after multiple attempts
			#   SGD is found to be most effective because
			#	  the loss significantly decreases after each epoch
			optimizer= Optimizer,
			metrics=['acc'])

from tensorflow.keras.preprocessing.image import ImageDataGenerator

# rescaling all image to 1/255.0
normalization = ImageDataGenerator(rescale = 1/255.0)

imageData_trainerGenerator = normalization.flow_from_directory(

	# path to store the training data set
	"/home/kiroslo/deepLearningFinalProject/FINALPROJECT--CS003C/training_data_set",

	# input size of the images
	target_size =(300, 300),

	# each batch : total number / 30
	batch_size = 30,

	# all images are stored as binary
	class_mode = 'binary')

training = model.fit_generator(
	imageData_trainerGenerator,

	# More epoch , the diminizing law will impact more
	epochs=8,
	verbose=1
		)

# Saving the model to a Hierarchical Data Forma 5 file
model.save('trainedModel-finalProduct.h5')

# Calling the class
if __name__ == "__main__":
	trainedModel()

