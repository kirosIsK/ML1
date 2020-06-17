"""
Webscrapping the internet

and automatically downloads human and champanzee files

Copyright by Wing Cheong Lo (c), 2019

webscrapping.py -- make recursive web scrapping
                    download image and predict if they
                    are monkeys or human
"""

from urllib.request import urlopen

# for web scrapping
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import lxml
import requests
import urllib.request
import sys
from tkinter import messagebox as msg
import tkinter as tk
from keras.preprocessing import image
import tensorflow as tf 
from tkinter import font
import numpy as np
import cv2
import os


class onlineSuperImageRaider:

    # Constructor
    def __init__(self):

        # The set to store filename 
        #   Set cannot have duplicate elements
        #   Therefore every Element on fileName list
        #   must be unique
        self.fileNameList_for_storing_download_images = set()
        self.automaticallyFileNameGenerator()

        # Read the URL and search targets
        #   if webpages are visited the web
        #   scrapping will stop visiting
        self.visited_web_page = set()

        # A request session
        #  Provide cookie consistence, connecting-pooling and configuration
        self.sessionPermission = requests.Session()

        # The beginning website starts to web scrapping
        self.websiteAttemptingToVisit = ''

        # Turning off SSL warnings
        #   SSL warnings may potentically disable web scrapping
        requests.packages.urllib3.disable_warnings()

        self.model = tf.keras.models.load_model('/home/kiroslo/machineLearning/FINALPROJECT--CS003C/Great_AI_Council/trainedModel-noCNN.h5')


    # An automatical method that both surf the website
    #   which is arted by recursion
    def webscrapping(self, url):

        # The beginning website starts to web scrapping
        self.websiteAttemptingToVisit = url

        # raise an error if a website has already visited
        if self.websiteAttemptingToVisit in self.visited_web_page:
            print ("This website has been seached")
            return None

        # adding the url into the set
        self.visited_web_page.add(self.websiteAttemptingToVisit)

        # visit the website via beautifulSoup in lxml feature
        content = self.sessionPermission.get(self.websiteAttemptingToVisit, verify=False).content
        soup = BeautifulSoup(content, features="lxml")

        # searching every images
        #   select find multiple instances and returns a list
        #   this part is particularly finding the 
        #       src for the image
        for img in soup.findAll('img'):
            img_src = str(img.get("src"))

            # calling the method with the joined url
        
            """
            # picking the first fileName from the fileNameList because it
            #   is randomly assigned
            import random
            fileName = random.choice(tuple(self.fileNameList_for_storing_download_images))
            print(fileName)

            """
            import random

            print(img_src)

            # the path to the folder of the downloaded image
            path = '/home/kiroslo/machineLearning/FINALPROJECT--CS003C/downloaded_Folder/folder_of_image'

            # randomly pick a filename from the tuple
            fileName = random.choice(tuple(self.fileNameList_for_storing_download_images))

            # Opening the URL
            request = urllib.request.Request(img_src, headers={'User-Agent': 'Mozilla/5.0'})
            result = urllib.request.urlopen(request)

            # Read the image
            binary_data = result.read()
            
            # Store the image to be bytearray
            byte_array = bytearray(binary_data)

            # Change all bytearray to uint8 because cv2.imwrite only take 8 bits
            numpy_array = np.asarray(byte_array, dtype = "uint8")
            imageFile = cv2.imdecode(numpy_array, cv2.IMREAD_UNCHANGED)

            # Store the image in the downloaded_Folder
            cv2.imwrite(os.path.join(path, fileName), imageFile)

            # predicting the percentage to be a human
            # changing all values of pixels to be between 0.0 to 1.0
            from tensorflow.keras.preprocessing.image import ImageDataGenerator
            normalization = ImageDataGenerator(rescale = 1/255.0)
                
            # loading the ImageDataGenerator
            testData_Generator = normalization.flow_from_directory(
            '/home/kiroslo/machineLearning/FINALPROJECT--CS003C/downloaded_Folder',
            target_size = (300,300),
            batch_size = 1,
            class_mode = 'binary')

            scores = self.model.predict(testData_Generator)

            import shutil

            # print the probaility of a downloaded photo 
            print("The percentage of this dude to be a human:", scores[0])

            if scores[0] > 0.8:
                shutil.move(os.path.join(path, fileName), os.path.join('/home/kiroslo/machineLearning/FINALPROJECT--CS003C/valid_photo', fileName))

            elif scores[0] < 0.2:
                shutil.move(os.path.join(path, fileName), os.path.join('/home/kiroslo/machineLearning/FINALPROJECT--CS003C/wrong_photo', fileName))

            else:
                os.remove(os.path.join(path, fileName))

            # removing the nametag of fileName from the fileNameList
            self.fileNameList_for_storing_download_images.remove(fileName)

            # Breaking no file
            if len(self.fileNameList_for_storing_download_images) == 0:
                print("Totally 10000 images has been downloaded")
                sys.exit()


        # Going ahead to next url
        for i in soup.select("a[href]"):
            self.webscrapping(urljoin(url, i["href"]))


    # method to automatically generate a number list
    def automaticallyFileNameGenerator(self) :

        # number for data_set_image that to downloads
        NUMBER_OF_DATA_SET_IMAGE = 10000

        # adding NUMBER_OF_DATA_SET_IMAGE to the 
        #   fileName number list
        for i in range (NUMBER_OF_DATA_SET_IMAGE):  

            # Taking the sys.maxsize to be int max
            #   because there is no maximum number in python
            INT_MAX = sys.maxsize

            from random import randint
            fileName = str(randint(0,INT_MAX)) + '.jpg'
            self.fileNameList_for_storing_download_images.add(fileName)


# class for webscrapping
#   a subclass for tkinter
class webscrappingGUI(tk.Tk):
    
    def __init__(self):

        # instance variable for url link
        self.url_link = ''

        # default font for all words
        self.default_font = font.Font(family="ubuntu", size=25, weight=font.BOLD)

        # extra window
        self.topLevel = tk.Toplevel(height=1200,width=1200, bg='lightyellow')

        # toplevel label
        self.tkLabel = tk.Label(self.topLevel, text="Enter a URL", font = self.default_font).grid(row=0, column=0)

        # text variable
        self.text_variable = tk.StringVar()

        # Entry
        self.topLevel_ENTRY = tk.Entry(self.topLevel, font = self.default_font, textvariable=self.text_variable)
        self.topLevel_ENTRY.grid(row=0, column=1)

        # Confirm button
        self.topLevel_confirm_button = tk.Button(self.topLevel, text="Confirm", command=self.automatical_webscrapping, font=self.default_font)
        self.topLevel_confirm_button.grid(row=0, column=2)
        

    # function for automatical web scrapping
    def automatical_webscrapping(self):

        self.url_link = self.topLevel_ENTRY.get()
        dataset_collector = onlineSuperImageRaider()
        
        try:
            dataset_collector.webscrapping(self.url_link)

        # when an empty input is entered, show an error
        except requests.exceptions.MissingSchema:

            # text window to show Invalid URL
            topLevel = tk.Toplevel(height=1200,width=1200, bg='lightyellow')
            topLevel_text = tk.Label(topLevel, text=("Warning: Invalid URL"), font=self.default_font, bg='lightyellow')
            topLevel_text.pack()
            topLevel.destroy()

        # when the raid! button is pressed twice
        except RuntimeError:

            # text window to show Invalid input
            topLevel = tk.Toplevel(height=1200,width=1200, bg='lightyellow')
            topLevel_text = tk.Label(topLevel, text=("Warning: Button cannot be clicked twice"), font=self.default_font, bg='lightyellow')
            topLevel_text.pack()
            topLevel.destroy()


# function to call class webscrappingGUI
def calling_object_webscapper():
    
    new_scrapper = webscrappingGUI()

    

    

        


