
ACKNOWLEDGE
===========
 This project is created by Wing Cheong Lo, July 2019, on his cs003c course under
	the supervision of professor Jamal Ashref. The editor himself receives lots of 
	support from Mr Ashref and is grateful for his guildance, This project aims to 
	distinguish a photo containg a humanoid object and make a decision of whether the
	object is a human or a champanzee/monkey. 

	Limited by the skill of the creator, this project may not be highly accurate 
	and can only distinguish a human and champanzee. Multiple class object
	identification is very hard to be made in the area of deep learning because
	if requires lots of data training. The project has not used of transfer learning.

 This project is honored to use datasets from the following organization
        and as a requirement of the dataset provider, this program will make citations.
  
        All dataset provider have stated that the dataset 
		❌️ SHOULD NOT BE commerical uses and
	    ✔️ should only be used on research or education.

This project is made of 11 self trained models, in order to find model with highest
	accuracy and lowest loss, while all the training images are the same

	CNN is applied in most of the model, however, application may result in 
	  inaccuracy as wel. But it reduces the time for training as well.

This project aims at making a automatical web scrapper which is able to distinguish a
	human and a champanzee.


RESULT
============
Probability generated by model.predict is used an indication to incidate whether
	object inside a photo is a human or champanzee. 
	If an object has a rating higher than 0.5 it is more likely to be a human (highest 1.0).
	If an object has a rating less than 0.5 it is more likely to be a champanzee (lowest 0.0).

Fur of champanzee is targeted as an indication to tell the computer that it is a champanzee ,
	while human has less fur.

	optimizer among SGD, Adam, RMSprop because it effectively reduces loss after each epoch.

	For the input layer, all images are in the input shape (300,300,3), which means 300x300x3 RGB pixels
	For the hiddle layer, usually 2 convolution and pooling are implements, and 2 hiddle layers each
		with 256 neutrons are densed.
	For the output layer, both sigmoid and softmax are implements. But sigmoid functions better than
		softmax in terms of two class clarification
	
	For the loss, binary_crossentropy is selected

During the research, the editor found that model trainedModel--noCNN (no convolutional network)
 has the highest prob to diagnose a human object from a photo taken by the webcam. This may
 highly because pooling and convolution have reduced the amount of informations in the photo.
 Therefore, all informations inside a selfie are retained when no convolutional neural network is used


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
					👉️https://www.kaggle.com/slothkong/10-monkey-species

					(contribute approximately 1400 images for the 10 speices of monkey with different poses and color)
				
				

=========
