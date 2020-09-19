from __future__ import print_function

from flask import Flask, render_template, request

import pandas as pd
from PIL import Image
import os
import io
from time import sleep
import pandas as pd
import cv2
from flask import Flask, render_template, request,jsonify, send_from_directory
import ftfy
import json
import re
import io
import csv
import sys
import glob
from flask import send_file
from tensorflow.lite.python.interpreter import Interpreter
import tensorflow as tf
import numpy as np
import requests
import json
input_mean = 127.5
input_std = 127.5
# Read TensorFlow Lite model from TensorFlow Lite file.
with tf.io.gfile.GFile('model.tflite', 'rb') as f:
  model_content = f.read()
with open("labels.txt", 'r') as f:
    labels = [line.strip() for line in f.readlines()]

# Initialze TensorFlow Lite inpterpreter.
interpreter = Interpreter(model_content=model_content)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
height = input_details[0]['shape'][1]
width = input_details[0]['shape'][2]
input_index = interpreter.get_input_details()[0]['index']
output = interpreter.tensor(interpreter.get_output_details()[0]["index"])
floating_model = (input_details[0]['dtype'] == np.float32)


application = app = Flask(__name__)  

UPLOAD_FOLDER = os.path.basename('.')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens):
    
    # Reading an image in default mode 
    image = cv2.imread("plain-white-background.jpg") 
        
    # Window name in which image is displayed 
    window_name = 'Image'
      
 
      
    # font 
    font = cv2.FONT_HERSHEY_SIMPLEX 
      
    # org 
    org = (500, 800) 

      
    # fontScale 
    fontScale = 2
       
    
      
    # Line thickness of 2 px 
    thickness = 4
       
    # Using cv2.putText() method 
    image = cv2.putText(image, "Nutri Grade:{}".format(nutri_grade), org, font, fontScale,  
                     (0, 0, 255) , thickness, cv2.LINE_AA, False) 
      
    # Using cv2.putText() method 
    image = cv2.putText(image, "Fat(100gr):{}".format(fat), (500,700), font, fontScale, 
                      (0, 255, 0) , thickness, cv2.LINE_AA, False)
    image = cv2.putText(image, "Protein(100gr):{}".format(protein), (500,600), font, fontScale, 
                      (255, 0, 0) , thickness, cv2.LINE_AA, False)
    image = cv2.putText(image, "Sugar(100gr):{}".format(sugar), (500,500), font, fontScale, 
                      (255, 255, 0) , thickness, cv2.LINE_AA, False)
    image = cv2.putText(image, "Salt(100gr):{}".format(salt), (500,400), font, fontScale, 
                      (255, 0, 255) , thickness, cv2.LINE_AA, False)
    image = cv2.putText(image, "Fiber(100gr):{}".format(fiber), (500,300), font, fontScale, 
                      (0, 255, 255) , thickness, cv2.LINE_AA, False)
    image = cv2.putText(image, "Allergens:{}".format(allergens), (500,200), font, fontScale, 
                     (125, 0, 255) , thickness, cv2.LINE_AA, False)
    
      
    #write the image
    
    cv2.imwrite("result.jpg", image)
    # open the image 
    Image1 = Image.open('result.jpg') 
      
    # make a copy the image so that the  
    # original image does not get affected
    if nutri_grade == 'a':
        
        Image1copy = Image1.copy() 
        Image2 = Image.open('static/images/A.jpg') 
        Image2copy = Image2.copy() 
          
        # paste image giving dimensions 
        Image1copy.paste(Image2copy, (0, 0)) 
          
        # save the image  
        Image1copy.save('static/images/final.png')
    elif nutri_grade == 'b':
        
        Image1copy = Image1.copy() 
        Image2 = Image.open('static/images/B.jpg') 
        Image2copy = Image2.copy() 
          
        # paste image giving dimensions 
        Image1copy.paste(Image2copy, (0, 0)) 
          
        # save the image  
        Image1copy.save('static/images/final.png')
    elif nutri_grade == 'c':
        
         
         Image1copy = Image1.copy() 
         Image2 = Image.open('static/images/C.jpg') 
         Image2copy = Image2.copy() 
          
        # paste image giving dimensions 
         Image1copy.paste(Image2copy, (0, 0)) 
          
        # save the image  
         Image1copy.save('static/images/final.png')
    elif nutri_grade == 'd':
         
         Image1copy = Image1.copy() 
         Image2 = Image.open('static/images/C.jpg') 
         Image2copy = Image2.copy() 
           
        # paste image giving dimensions 
         Image1copy.paste(Image2copy, (0, 0)) 
          
        # save the image  
         Image1copy.save('static/images/final.png')
    elif nutri_grade == 'e':
         
         Image1copy = Image1.copy() 
         Image2 = Image.open('static/images/E.jpg') 
         Image2copy = Image2.copy() 
          
        # paste image giving dimensions 
         Image1copy.paste(Image2copy, (0, 0)) 
          
        # save the image  
         Image1copy.save('static/images/final.png')
    else:
        cv2.imwrite("'static/images/final.png'", image)
        





    
   
def get_url(food,brand):
    url_get = ' https://www.brocade.io/api/items?query={}+{}'.format(food,brand)
    headers_get = {'Accept' : 'application/json'}
    resp = requests.get(url_get,headers = headers_get)
    r = resp.json()
    if len(r) == 0:
        
          url_get = ' https://www.brocade.io/api/items?query={}'.format(food)
          headers_get = {'Accept' : 'application/json'}
          resp = requests.get(url_get,headers = headers_get)
          r = resp.json()
          gtin = r[0]["gtin14"]
       
          url_get = "https://nutritions.lab.atrify.com/nutrition/%s" % (gtin)
          headers_get = {'apikey' : 'fd9653ad-6cf1-4ade-8524-d90a1c709432','Accept' : 'application/json'}
          resp = requests.get(url_get,headers = headers_get)
          r = resp.json()
          nutri_grade = r['nutriScoreGrade']
          energy = r['energy100Kcal']
          fat = r['fat100gr']
          protein = r['protein100gr']
          sugar = r['sugar100gr']
          salt = r['salt100gr']
          fiber = r['fiber100gr']
          allergens = r['allergens']
                
          return nutri_grade,fat,protein,sugar,salt,fiber,allergens
        
          
    try:
        
        
        
         gtin = r[0]["gtin14"]
   
         url_get = "https://nutritions.lab.atrify.com/nutrition/%s" % (gtin)
         headers_get = {'apikey' : 'fd9653ad-6cf1-4ade-8524-d90a1c709432','Accept' : 'application/json'}
         resp = requests.get(url_get,headers = headers_get)
         r = resp.json()
         nutri_grade = r['nutriScoreGrade']
         energy = r['energy100Kcal']
         fat = r['fat100gr']
         protein = r['protein100gr']
         sugar = r['sugar100gr']
         salt = r['salt100gr']
         fiber = r['fiber100gr']
         allergens = r['allergens']
                
         return nutri_grade,fat,protein,sugar,salt,fiber,allergens
        
    except:
        
        
          
        gtin = r[1]["gtin14"]
   
        url_get = "https://nutritions.lab.atrify.com/nutrition/%s" % (gtin)
        headers_get = {'apikey' : 'fd9653ad-6cf1-4ade-8524-d90a1c709432','Accept' : 'application/json'}
        resp = requests.get(url_get,headers = headers_get)
        r = resp.json()
        nutri_grade = r['nutriScoreGrade']
        energy = r['energy100Kcal']
        fat = r['fat100gr']
        protein = r['protein100gr']
        sugar = r['sugar100gr']
        salt = r['salt100gr']
        fiber = r['fiber100gr']
        allergens = r['allergens']
                
        return nutri_grade,fat,protein,sugar,salt,fiber,allergens
   

 
@app.route('/')  
def file():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':
        text = request.form['text']
        processed_text = text.upper()
        print(processed_text)
  

        file = request.files['file']
            # retrieve file from html file-picker
        upload = request.files.getlist("file")[0]
        print("File name: {}".format(upload.filename))
        filename = upload.filename

        # file support verification
        ext = os.path.splitext(filename)[1]
        if (ext == ".jpg") or (ext == ".jpeg") or (ext == ".png") or (ext == ".bmp"):
            print("File accepted")
            file.filename = "static/images/temp.jpg"
            file.save(file.filename)
        else:
            return render_template("error.html", message="The selected file is not supported"), 400
        # Pre-processing should remain the same. Currently, just normalize each pixel value and resize image according to the model's specification.
        image_initial = cv2.imread("static/images/temp.jpg")
        image = cv2.resize(image_initial, (width, height))
        # Add batch dimension and convert to float32 to match with the model's input
        # data format.
        image = np.expand_dims(image, axis=0)
        if floating_model:
            
            image = (np.float32(image) - input_mean) / input_std

        # Run inference.
        interpreter.set_tensor(input_index, image)
        interpreter.invoke()


        # Post-processing: remove batch dimension and find the label with highest
        # probability.
        predict_label = np.argmax(output()[0])
        object_name = labels[int(predict_label)]
        print(object_name)
        if object_name == "BEANS":
            nutri_grade,fat,protein,sugar,salt,fiber,allergens = get_url('BEANS',processed_text)
            add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens)
            
        elif object_name == "CAKE":
            nutri_grade,fat,protein,sugar,salt,fiber,allergens = get_url('CAKE',processed_text)
            add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens)
           
        elif object_name == "CANDY":
            nutri_grade,fat,protein,sugar,salt,fiber,allergens = get_url('CANDY',processed_text)
            add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens)
          
        elif object_name == "CEREAL":
            nutri_grade,fat,protein,sugar,salt,fiber,allergens = get_url('CEREAL',processed_text)
            add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens)
            
        elif object_name == "CHIPS":
            nutri_grade,fat,protein,sugar,salt,fiber,allergens = get_url('CHIPS',processed_text)
            add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens)
            
        elif object_name == "CHOCOLATE":
         
            nutri_grade,fat,protein,sugar,salt,fiber,allergens = get_url('CHOCOLATE',processed_text)
            add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens)
         
        elif object_name == "COFFEE":
            nutri_grade,fat,protein,sugar,salt,fiber,allergens = get_url('CANDY',processed_text)
            add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens)
        
        elif object_name == "CORN":
            nutri_grade,fat,protein,sugar,salt,fiber,allergens = get_url('CORN',processed_text)
            add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens)
         
        elif object_name == "FISH":
            nutri_grade,fat,protein,sugar,salt,fiber,allergens = get_url('FISH',processed_text)
            add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens)
          
        elif object_name == "FLOUR":
            nutri_grade,fat,protein,sugar,salt,fiber,allergens = get_url('FLOUR',processed_text)
            add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens)
           
        elif object_name == "HONEY":
            nutri_grade,fat,protein,sugar,salt,fiber,allergens = get_url('HONEY',processed_text)
            add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens)
           
        elif object_name == "JAM":
            nutri_grade,fat,protein,sugar,salt,fiber,allergens = get_url('JAM',processed_text)
            add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens)
           
        elif object_name == "JUICE":
            nutri_grade,fat,protein,sugar,salt,fiber,allergens = get_url('JUICE',processed_text)
            add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens)
         
        elif object_name == "MILK":
            nutri_grade,fat,protein,sugar,salt,fiber,allergens = get_url('MILK',processed_text)
            add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens)
          
        elif object_name == "NUTS":
            nutri_grade,fat,protein,sugar,salt,fiber,allergens = get_url('NUTS',processed_text)
            add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens)
           
        elif object_name == "OIL":
            nutri_grade,fat,protein,sugar,salt,fiber,allergens = get_url('OIL',processed_text)
            add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens)
       
        elif object_name == "PASTA":
            nutri_grade,fat,protein,sugar,salt,fiber,allergens = get_url('PASTA',processed_text)
            add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens)
            
        elif object_name == "RICE":
            nutri_grade,fat,protein,sugar,salt,fiber,allergens = get_url('RICE',processed_text)
            add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens)
           
        elif object_name == "SODA":
            nutri_grade,fat,protein,sugar,salt,fiber,allergens = get_url('SODA',processed_text)
            add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens)
          
        elif object_name == "SPICES":
            nutri_grade,fat,protein,sugar,salt,fiber,allergens = get_url('SPICES',processed_text)
            add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens)
            
        elif object_name == "SUGAR":
            nutri_grade,fat,protein,sugar,salt,fiber,allergens = get_url('SUGAR',processed_text)
            add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens)
         
        elif object_name == "TEA":
            nutri_grade,fat,protein,sugar,salt,fiber,allergens = get_url('TEA',processed_text)
            add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens)
         
        elif object_name == "TOMATO_SAUCE":
            nutri_grade,fat,protein,sugar,salt,fiber,allergens = get_url('TOMATO_SAUCE',processed_text)
            add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens)
           
        elif object_name == "VINEGAR":
            nutri_grade,fat,protein,sugar,salt,fiber,allergens = get_url('VINEGAR',processed_text)
            add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens)
          
        elif object_name == "WATER":
            nutri_grade,fat,protein,sugar,salt,fiber,allergens = get_url('WATER',processed_text)
            add_text(nutri_grade,fat,protein,sugar,salt,fiber,allergens)
           
        
        return send_image('final.png')




# retrieve file from 'static/images' directory
@app.route('/static/images/<filename>')
def send_image(filename):
    return send_from_directory("static/images", filename)

  




application.run(host='0.0.0.0',debug=True)




