import numpy as np
import pandas as pd
import torch
from torch import nn
from torch.utils.data import Dataset,DataLoader
from torchvision import transforms

#dataset for trainset
class StockData_Train(Dataset):
    def __init__(self):
        df = pd.read_csv('data/train_reg.csv')
        self.x = torch.tensor(df.iloc[:,:-1].values,dtype=torch.float)
        self.y = torch.tensor(df.iloc[:,-1].values,dtype=torch.float)
        self.n_samples = df.shape[0]
    
    def __getitem__(self,index):
        return self.x[index],self.y[index]

    def __len__(self):
        return self.n_samples

#dataset for test set
class StockData_Test(Dataset):
    def __init__(self):
        df = pd.read_csv('data/test_reg.csv')
        self.x = torch.tensor(df.iloc[:,:-1].values,dtype=torch.float)
        self.y = torch.tensor(df.iloc[:,-1].values,dtype=torch.float)
        self.n_samples = df.shape[0]
    
    def __getitem__(self,index):
        return self.x[index],self.y[index]

    def __len__(self):
        return self.n_samples

trainset = StockData_Train()
testset = StockData_Test()

loadtrain = DataLoader(trainset,shuffle=True,batch_size=30)
loadtest = DataLoader(testset,batch_size=30)



