import numpy as np
import pandas as pd
import torch
from torch import nn
from torch.utils.data import Dataset,DataLoader
from torchvision import transforms
from sklearn.model_selection import train_test_split

#time series generator
def timeseries(path,steps):
    df = pd.read_csv(path)
    result = []
    # arr = np.array((steps,df.shape[1]-3))
    for step in range(0,df.shape[0]-steps+1,steps+1):
        arr = np.zeros((steps,df.shape[1]-3))
        for i in range(steps):
            arr[i,:] = df.iloc[step+i,3:]
        arr1 = arr.flatten()
        results = np.append(arr1,df.iloc[step+steps,2])
        result.append(results)
    df= pd.DataFrame(result)
    file_path = 'data/series.csv'
    df.to_csv(path,index=False)

    return file_path

def splitter(path):
    df= pd.read_csv(path)
    x = df.iloc[:,:-1]
    y = df.iloc[:,-1]
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
    test = pd.concat([x_test,y_test],axis=1,ignore_index=True)
    train = pd.concat([x_train,y_train],axis=1,ignore_index=True)
    test.to_csv('data/test.csv',index=False)
    train.to_csv('data/train.csv',index=False)



# filepath = timeseries('Stock_data/data/turkish_stocks.csv',5)
# splitter(filepath)

#regular train and test splitter
def splitter_reg(path):
    df= pd.read_csv(path)
    x = df.iloc[:,3:]
    y = df.iloc[:,2]
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
    test = pd.concat([x_test,y_test],axis=1,ignore_index=True)
    train = pd.concat([x_train,y_train],axis=1,ignore_index=True)
    test.to_csv('data/test_reg.csv',index=False)
    train.to_csv('data/train_reg.csv',index=False)

splitter_reg('Stock_data/data/turkish_stocks.csv')
