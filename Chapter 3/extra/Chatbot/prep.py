import spacy

import numpy as np
from torch.utils.data import DataLoader,Dataset

nlp=spacy.load('en_core_web_sm')


def tokenizer(sentence):
    """
    takes text - string
    returns list of lemmatized words of that text

    """
    doc = nlp(sentence)
    tokens = [token.lemma_ for token in doc if not token.is_punct]
    return tokens


def prep(chats):
    """
    takes dictionary of chat patterns,
    returns (tokenized sentences,labels) , vocabulary of words, and unique tags
    """
    tags = []
    patterns = []
    voca = []
    pairs = []
    for intent in chats['intents']:
        tags.append(intent['tag'])
        for pattern in intent['patterns']:
            tokens = tokenizer(pattern)
            w = [token for token in tokens if not token in voca]
            voca.extend(w)
            pairs.append((tokens,intent['tag']))
  
    return pairs,voca,tags


def embed(voca,sentence):
    '''
     1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bag   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    '''
    bag =np.zeros(len(voca),dtype=np.float32)
    for idx,w in enumerate(voca):
        if w in sentence:
            bag[idx] += 1
    return bag

def tokenize(pairs,voca,tags):
    """
    takes pairs (tokenized text, proper tag), vocab and label tags
    returns embedded inputs and labels
    """
    xs = []
    labels = []
    for pair in pairs:
        # getting x and labels
        x,y = pair

        #embedding
        x = embed(voca,x)
        y = tags.index(y)
        xs.append(x)
        labels.append(y)
    return xs,labels

class CusDatset(Dataset):
    
    def __init__(self,xs,labels):
        self.len = len(xs)
        self.xs = xs
        self.labels = labels

    def __getitem__(self,ind):
        return self.xs[ind],self.labels[ind]
    def __len__(self):
        return self.len


def loader(x,y,batchsize):
    """
    takes, embedded inputs x, label y and batch size as input
    return torch dataloader

    """
    set = CusDatset(x,y)
    return DataLoader(set,batch_size=batchsize,shuffle=True)


def input_prep(text,voca):
    """
    takes user string input, voca as inputs
    returns embedded version of  that string
    """
    tokens = tokenizer(text)
    x_test = embed(voca,tokens)
    return x_test