
from scipy.sparse.construct import rand
from torchtext import datasets
import pandas as pd
import numpy as np
import spacy
from torch.utils.data import DataLoader,Dataset
import torch
from torch import nn
import  torch.nn.functional as F
from sklearn.model_selection import train_test_split
from torchtext.vocab import FastText

vec = FastText('simple')
## loading 
def load(path):
    """
    takes - path str
    returns -> features-ndarray and labels-ndarray
    """
    df = pd.read_csv(path,header=None,nrows=1000)
    # ordinal embedding targets
    func = lambda x: x-1
    df['stars'] = df[0].apply(func)
    #mergin'
    df['reviews'] = df.iloc[:,1]+ ' ' + df.iloc[:,2]
    #dropping
    df.drop([0,1,2],axis=1,inplace=True)

    return df['reviews'].values,df['stars'].values

## splitting
def split(path,test_size=0.2):
    '''
    takes path, test ratio
    returns x_tr, x_val, y_train, y_val
    '''
    x,y = load(path)
    print('splitted')

    return train_test_split(x,y,test_size=test_size,random_state=0)

## prep
def prep(text):
    nlp =spacy.load('en_core_web_sm')
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_punct and not token.is_stop]
    return tokens


# encoding 
def token_encoder(token,vec):
    if token == '<pad>':
        return 1
    else:
        try:
            return vec.stoi[token]
        except:
            if type(token) != str :
                print(f'expected str, but got {type(token)} instead.')
            else:
                return 0

def text_encoder(tokens,vec):
    '''
    input - list of lemmatized tokens
    returns - list of encoded tokens
    '''
    return [token_encoder(token,vec) for token in tokens]

## padding
def padding(list_indexed,max_length=32,pad=1):
    #padding short reviews
    res = list_indexed + (max_length - len(list_indexed))*[pad]
    # slicing prior to return, if review is longer
    return res[:max_length]

##  custom dataset
class CustomDataset(Dataset):
    def __init__(self,x,y,max_length=32):
        self.max_length = max_length
        self.vec = FastText('simple')
        self.vec.vectors[0] = torch.zeros(self.vec.vectors[0].shape[0])
        self.vec.vectors[0] = -torch.ones(self.vec.vectors[0].shape[0])
        self.labels = y
        self.inputs = [padding(text_encoder(prep(review),self.vec),self.max_length) for review in x]
        

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, i):
        assert len(self.inputs[i]) == self.max_length
        return self.inputs[i],self.labels[i]

## custom collate function
def collate(batch,vectorizer=FastText('simple').vectors):
    #inner torch.stack is stacking vectorized words into review tensor
    #outer torch.stack is stacking that review into batch tensor
    inputs = torch.stack([torch.stack([vectorizer[token] for token in item[0]]) for item in batch])
    #
    #converting labels into Long type tensors, as criterion functions expects that dtype
    labels = torch.LongTensor([item[1] for item in batch])
    return inputs, labels

def loader(x,y):
    valset = CustomDataset(x,y)
    return DataLoader(valset,batch_size=64,collate_fn=collate)

## function to genereate loader for test,validation and test
def all_data_loaders(train_path,test_path):
    
    x_test,y_test = load(test_path)
    x_train,x_val,y_train,y_val = split(train_path)
    print('in all loader')

    return loader(x_train,y_train), loader(x_val,y_val), loader(x_test,y_test)

