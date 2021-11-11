from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from joblib import load


pat = 'web_app/static/uploads/input.csv'
def predicts(path):
    model = load('web_app/static/uploads/model.joblib')
    X_test = pd.read_csv(path)
    X_test.drop('Unnamed: 0',axis=1,inplace=True)
    predict = model.predict(X_test)
    unique, counts = np.unique(predict,return_counts=True)
    vals = unique.tolist()
    cs = counts.tolist()
    result = {val:c for val,c in zip(vals,cs) }
    return result

def rec(path=pat):
    counts= predicts(path)
    
    b,d,s,t,w = counts['Bus'],counts['Car'],counts['Still'],counts['Train'],counts['Walking']

    result = [round((b*5)/60,1),
    round((d*5)/60,1),
    round((s*5)/60,1),
    round((t*5)/60,1),
    round((w*5)/60,1)]
    

    return result
    