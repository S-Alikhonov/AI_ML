from PIL import Image
import numpy as np
import pandas as pd
import os
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt

def get_images():
    path = "data/trainingSet/trainingSet/"
    tr_directory = os.listdir(path)[1:]
    df = []
    for dir in tr_directory:
        filenames = os.listdir(f"{path}{dir}")
        for filename in filenames:
            img = Image.open(f"{path}{dir}/{filename}")
            arr=np.array(img).astype(float).flatten()
            #adding labels to the image array
            arr= np.append(arr,float(dir))
            df.append(arr)
    images = pd.DataFrame(df)
    return images


def image_to_feed(img_path):
    image = Image.open(img_path)
    #in our dataset, samples comes as a row vector, so test also should be in that form
    img_arr = np.array(image).astype(float).flatten().reshape(1,-1)

    return img_arr

def show_image(img_path,predict):
    image = image_to_feed(img_path)
    side = int(np.sqrt(image.shape[1]))
    image = image.reshape((side,side))
    imshow(image)
    plt.title(f"model predicted it as {predict}")
    plt.show()



