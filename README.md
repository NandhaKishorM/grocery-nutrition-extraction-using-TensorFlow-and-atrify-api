# grocery-nutrition-extraction-using-TensorFlow-and-atrify-api
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1i8cx1MoZJ_nucTZ3jJz5ftsXrknq4zNu?usp=sharing)

# Training a classification model
1. **Dataset**
https://github.com/PhilJd/freiburg_groceries_dataset

**Total number of classes: 25**

1. BEANS
2. CAKE
3. CANDY
4. CEREAL
5. CHIPS
6. CHOCOLATE
7. COFFEE
8. CORN
9. FISH
10. FLOUR
11. HONEY
12. JAM
13JUICE
14. MILK
15. NUTS
16. OIL
17. PASTA
18. RICE
19. SODA
20. SPICES
21. SUGAR
22. TEA
23. TOMATO_SAUCE
24. VINEGAR
25. WATER

To train the model use this link : [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1i8cx1MoZJ_nucTZ3jJz5ftsXrknq4zNu?usp=sharing)

# Run
To run use this, colab link: [![Open In Colab](https://colab.research.google.com/drive/1igsk90OEHhG6eQLhzyBFY5IeDtmu89Jq?usp=sharing)

![alt_text](https://github.com/kishorkuttan/grocery-nutrition-extraction-using-TensorFlow-and-atrify-api/blob/master/main.png)
## Result
![alt_text](https://github.com/kishorkuttan/grocery-nutrition-extraction-using-TensorFlow-and-atrify-api/blob/master/result_final.png)
## How we made it
1. First we train our model on efficient_net and made a tflite model file
2. Used it to make prediction on what is the grocery item is. ex: chocolate, soda etc.
3. Using the label name(chocolate,soda etc,) we made a query on brocade api to get gtin-14 number( https://www.brocade.io/api/items?query=$query). Intially we selected first and second gtin number
4. After getting the gtin-14 number we used atrify nutrient information api to get all the information about the product. Including fat, sugar, salt, allergence etc. 
5. We built a Flask RESTful API web application to make things smooth
6. But we failed to identify the brand name. Tought about applying OCR. Tried pytesseract. But accuracy is too low and then we tried AWS textract. Even the state of the art OCR engine failed to identify certain text. Then we move on with manual entry of brand name
# TO DO
1. We tried to use the Holoselecta data provided by **autoidlabs**,which include 109 classed for custom object detection training using TensorFlow. But the 2.1 GB dataset is too much for Google colab. We dropped the plan due to this limitation.
![alt_text](https://github.com/kishorkuttan/grocery-nutrition-extraction-using-TensorFlow-and-atrify-api/blob/master/data.png)
2. Training on object detection-SSD_Mobilenet_quantised model will helps to deploy offline mode on mobile application, Fast inference speed and much more.
3. Customer can just take the photo of the grocery shelf and all the information can be accessed in an instance


