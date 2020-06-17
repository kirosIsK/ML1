"""
GUI files for the project

Copyright by Wing Cheong Lo (c), 2019

GUI.py -- main design part 
"""

import tkinter as tk
from urllib.request import urlopen
# for web scrapping
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import lxml
import requests
import sys
from tkinter import messagebox as msg
import cv2
import os
import sys
from PIL import Image
import tensorflow as tf 
from keras.preprocessing import image
import numpy as np
import PIL
from loadingThetrainedModel import *
from ImageCapture import *
from tkinter import font
from webcscrapping import *
import time
import math


# sub class of tkinter 
class GUI(tk.Tk):
    def __init__(self):

        # inheriting all instance variable for the init
        super().__init__()

        # title of the project
        self.title("Final project CS003C")  

        # size of the main window
        self.geometry("2400x1600") 

        # default font     
        self.default_font = font.Font(family="ubuntu", size=25, weight=font.BOLD)
   
        # object : imageCaptureButton
        self.ImageCaptureButton = tk.Button(self, text="Human Verification!", command=webcamScreenShotFunction, font=self.default_font)

        # object : quitButton
        self.quitButton = tk.Button(self, text="Quit", bg="silver", fg="black", command=self.quitEvent, font=self.default_font)

        # object : webscrapper
        self.webscrapperButton = tk.Button(self, text="Raid!", bg="silver",command=calling_object_webscapper, font=self.default_font)

        # packing the quitButton on the main TK()
        self.webscrapperButton.pack(fill=tk.BOTH, expand=1)

        # packing the imageCaptureButton on the main TK()
        self.ImageCaptureButton.pack(fill=tk.BOTH, expand=1)

         # packing the quitButton on the main TK()
        self.quitButton.pack(fill=tk.BOTH, expand=1)

        # canvas for animation
        canvas= tk.Canvas(self, width=2400, height=800, bg='black')
        canvas.pack()

        # animation
        aBall = canvas.create_oval(20,20,100,100,fill="gold")
        bBall = canvas.create_oval(420,20,100,100,fill="white")

        self.time = 0

        # while the GUI is not closed
        while True:
            self.firstSpeed = 1
            self.secondSpeed = 2

            # To move east
            while 0 <= self.time < 2000:
                canvas.move(aBall,self.firstSpeed,0)
                canvas.move(bBall,self.firstSpeed,0)
                self.update()
                time.sleep(0.0001)
                self.time += 1

            # To move south
            while 2000 <= self.time < 2300:
                canvas.move(aBall,0,self.firstSpeed)
                canvas.move(bBall,0,self.firstSpeed)
                self.update()
                time.sleep(0.001)
                self.time += 1

            # To move west
            while 2300 <= self.time < 4300:
                canvas.move(aBall,-self.firstSpeed,0)
                canvas.move(bBall,-self.firstSpeed,0)
                self.update()
                time.sleep(0.001)
                self.time +=1

            # To move north
            while 4300 <= self.time < 4600:
                canvas.move(aBall,0,-self.firstSpeed)
                canvas.move(bBall,0,-self.firstSpeed)
                self.update()
                time.sleep(0.0005)
                self.time +=1

            self.time = 0


    # function that quit the program
    def quitEvent(self):

        # destroy the object
        self.destroy()

        # quit the system
        import sys
        sys.exit()

        