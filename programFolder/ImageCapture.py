""""
imageCapture program for the project

Copyright by Wing Cheong Lo (c), 2019

Imagecapture.py -- take a photo
"""
import cv2
import os
import tensorflow as tf 
from keras.preprocessing import image
import numpy as np
import PIL
from loadingThetrainedModel import loadingThetrainedModel

# function webcamScreenShotFunction
def webcamScreenShotFunction ():

    # window
    frameName = "HUMAN VERTIFICATION"

    # packing th ewindow
    cv2.namedWindow(frameName)

    # webcam capture a photo
    capturedImage = cv2.VideoCapture(0)

    # setting the height
    capturedImage.set(3,1200)

    # setting the width
    capturedImage.set(4,800)

    # opening a frame to read the photo
    if capturedImage.isOpened():
        firming,frame = capturedImage.read() 
    
    # steaming from the webcam
    while firming:

        # reading the video from frame
        firming,frame = capturedImage.read()

        # showing the steaming 
        cv2.imshow(frameName,frame)

        # press 'a' to take a photo
        if cv2.waitKey(33) == ord('a'):
            break

    # Path to store the photo
    path = '/home/kiroslo/machineLearning/FINALPROJECT--CS003C/ImageFolder/new1'

    # saving the photo in the path
    cv2.imwrite(os.path.join(path , 'webcamScreenShot.jpg'), frame)

    # calling the model to test whether the photo is recognized as a human
    #   a champanzee
    loadingThetrainedModel()

    # destroy the windown
    cv2.destroyWindow(frameName)

