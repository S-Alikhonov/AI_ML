import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize
import time

def timed(): #to calculate the time spent
    return time.time()

class KNN:
    def __init__(self, k): #initiating with k attribute
        self.k = k

    def euclidean_distances(self, v1, v2): #method to calculate vector norm
        return np.linalg.norm(v1-v2)

    def fit(self, x, y): #for knn , fitting is storing those value for later use
        self.x_train, self.y_train = x,y
        # self.x_train, self.y_train = normalize(x,axis=1),y #to normalize the values of data 
        return self

    def predict(self,X): # prediction part
        start = timed() 
        labels = []

        for i in X:
            X = normalize(X,axis=1) #to normalize the test data
            distances = []
            for j in self.x_train:
                d = self.euclidean_distances(i,j)
                distances.append(d)

            df = pd.DataFrame({'distances':distances, 'labels':self.y_train})
            
            l = df.sort_values('distances').head(self.k).groupby('labels').count().sort_values('distances', ascending=False).index[0]
            labels.append(l)

        stop = timed()
        self.time_spent = stop - start #time spent as attribute
        self.labels = np.array(labels)
        return self.labels
    
    def performance(self,y_test):#takes y_test, compares prediction and evaluates performance
        return sum(y_test == self.labels)/y_test.shape[0]
