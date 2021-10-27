from train import *
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder
import numpy as np

condition = True

while condition:
    age = int(input("How old are you? \n"))
    sex = input('what is your sex? \n')
    children = int(input("How many children do you have? \n"))
    smoker = bool(input("Do you smoke? \n"))
    bmi = float(input("what is your body bmi index? \n"))
    region = input('which region do you live in? (southwest,southeast,northwest,northeast) \n')

    data = pd.DataFrame({
        'age':[age],
        'sex':[sex],
        'bmi':[bmi],
        'children':[children],
        'smoker':[smoker],
        'region': [region]
    })
    X = data.values
    encoder = ColumnTransformer( [('ordinal', OrdinalEncoder(handle_unknown= 'use_encoded_value', unknown_value = -1), [1,4,5] )] )
    X = np.concatenate((X[:,[0,2,3]],encoder.fit_transform(X)),axis=1)
    best_model(X)
    
    willingness = input('do you want to continue?(y/n) \n')
    if willingness=='y':
        pass
    else:
        print('okay')
        break



