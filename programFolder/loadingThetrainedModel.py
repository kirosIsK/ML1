""""
loadingThetrainedModel program for the project

Copyright by Wing Cheong Lo (c), 2019

loadingThetrainedModel.py -- load a model
"""
import tensorflow as tf 
from keras.preprocessing import image
import numpy as np
import PIL
from PIL import Image
import os
import tkinter as tk
from tkinter import messagebox as msg
from tkinter import font


def loadingThetrainedModel():
    model = tf.keras.models.load_model('/home/kiroslo/machineLearning/FINALPROJECT--CS003C/Great_AI_Council/trainedModel-noCNN.h5')
    model.summary()

    from tensorflow.keras.preprocessing.image import ImageDataGenerator

    # changing all values of pixels to be between 0.0 to 1.0
    normalization = ImageDataGenerator(rescale = 1/255.0)

    testData_Generator = normalization.flow_from_directory(
	'/home/kiroslo/machineLearning/FINALPROJECT--CS003C/ImageFolder',
	target_size = (300,300),
	batch_size = 1,
	class_mode = 'binary'
)

    # predicting the percentage to be a human
    scores = model.predict(testData_Generator)

    # loading the webcam screenshoted image
    imageResult = Image.open('/home/kiroslo/machineLearning/FINALPROJECT--CS003C/ImageFolder/new1/webcamScreenShot.jpg')
    
    # showing the webcam screenshoted image
    imageResult.show()

    # percentage to be a human
    PROBABILITY_TO_BE_A_HUMAN = scores[0] * 100 // 1

    print("The percentage of this dude to be a human:", scores[0])

    # text window to show whether the object inside the window is a human or champanzee
    default_font = font.Font(family="ubuntu", size=40, weight=font.BOLD)
    topLevel = tk.Toplevel(height=1200,width=1200, bg='lightyellow')
    topLevel_text = tk.Label(topLevel, text=("Prob to be a human: %dpercent" % PROBABILITY_TO_BE_A_HUMAN), font=default_font)
    topLevel_text.pack(fill=tk.BOTH, expand=1)

    if scores[0]>0.5:
        result = 'human'
    else:
        result = 'Champanzee'

    # Case : result is a humam
    if result == "human":
        
        # PIL has some problem opening a png file
        imageResult = Image.open('/home/kiroslo/machineLearning/FINALPROJECT--CS003C/ImageFolder/Offspring.jpg')

        print("Yes!")
        
        # showing the result image
        imageResult.show() 

    # Case : result is a champanzee
    elif result == 'Champanzee':

        # PIL has no problem open a jpg file
        imageResult = Image.open('/home/kiroslo/machineLearning/FINALPROJECT--CS003C/ImageFolder/kingkongediited.jpg')
        
        # showing the result images
        imageResult.show()
