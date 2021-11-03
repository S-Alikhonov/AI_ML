from matplotlib.pyplot import show
import numpy as np
import pandas as pd
from joblib import load
from images import image_to_feed,show_image

#trained model
model = load('model.joblib')
#path to the image to predict
file = 'data/testSample/testSample/img_246.jpg'
test_image = image_to_feed('data/testSample/testSample/img_246.jpg')

predict = model.predict(test_image)[0]
show_image(file,predict)