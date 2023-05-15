#We Promise End to End Guidance in Your Projects
#This Project is created by developerkk
#For Information visit developerkk.in
#We are Providing Projects at very valuable Price
#We are Also Helping You in fixing Error and run your Project
import cv2
from keras.models import load_model
from PIL import Image
import numpy as np

model=load_model('BrainTumor10EpochsCategorical.h5')

image=cv2.imread('D:\\Deep Learning Project\\Brain Tumor Image Classification\\pred\\pred0.jpg')

img=Image.fromarray(image)

img=img.resize((64,64))

img=np.array(img)

input_img=np.expand_dims(img, axis=0)

result=model.predict_classes(input_img)
print(result)




