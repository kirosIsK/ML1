"""
Main program for the project

Copyright by Wing Cheong Lo (c), 2019

main.py -- maining access to the program
"""
import cv2
import os
import sys
from PIL import Image
import tensorflow as tf 
from keras.preprocessing import image
import numpy as np
import PIL
from GUI import GUI
import tkinter as tk
import pygame

# main class for the program
class main:

    # play a music.
    pygame.init()
    # pygame.mixer.init()
    # pygame.mixer.music.load('/home/kiroslo/machineLearning/FINALPROJECT--CS003C/programFolder/Happy Morning - AShamaluevMusic.mp3')
    # pygame.mixer.music.play()

    # GUI for the program
    graphical_user_interface = GUI()
    graphical_user_interface.mainloop()

# calling main class
if __name__ == "__main__":
    main()






