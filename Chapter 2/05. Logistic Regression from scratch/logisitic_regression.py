import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


class LogisticRegression_imp:

    #init
    def __init__(self,lr,n_iter):
        self.lr = lr
        self.n_inter = n_iter
        self.weight = None
        self.bias = None

    #private function, to create sigmoid funtion
    def __sigmoid(self,x):
        """
        function takes x as variable, and returns 
        its sigmoid function -> f(x) = 1 / (1 + e^(-x))
        """
        return 1/(1+np.exp(-x))
    
    #private function to generate linear function
    def __linear(self,X,W,B):
        """
        function takes variables, and returns linear function -> f(X) = W*X + B
        """
        return np.dot(W.T,X) + B

    #cost function generates cost function for model
    def __cost(self,y,y_p,m):
        return -(1/m)*np.sum(y*np.log(y_p) + (1-y)*np.log(1-y_p))

    #during number of iterations, seeks for value of wieght and bias that cost becomes minimum
    def fit(self,X,y):
        """
        fit function, takes features and labels (train samples)
        returns weights and bias for sigmoid function. 
        """
        X = X.T
        y = y.reshape(1,-1)
        m = y.shape[1]
        n = X.shape[0]
        self.weight = np.zeros((n,1))
        self.bias = 0
        cost_list = []

        for _ in range(self.n_inter):

            z = self.__linear(X,self.weight,self.bias)
            y_p = self.__sigmoid(z)
            cost = self.__cost(y,y_p,m)
            dW = (1/m) * np.dot(y_p-y,X.T)
            dB = np.sum(y_p - y)
            self.weight = self.weight - self.lr * dW.T
            self.bias = self.bias - self.lr * dB
            cost_list.append(cost)

        self.cost_list = cost_list

        return self
    #using bias and wieght, predicts labels out of test sample
    def predict(self,X):
        """
        predict method, takes test sample, and using weight and bias , return predicted labels. (test sample)-> predicted labels
        """
        X = X.T
        z = self.__linear(X,self.weight,self.bias)
        y_p = self.__sigmoid(z)
        y_p = y_p > 0.5
        y_p = np.array(y_p,dtype='int64')

        self.y_p = y_p
        return y_p
    #calculates model's accuracy
    def score(self,y):
        """
        score method takes test labels, compares it with model prediction and returns accuracy in percentage
        """
        return np.sum(self.y_p == y)/y.shape[0]


##### data collection
data  = load_breast_cancer()
df = pd.DataFrame(data.data,columns=data.feature_names)
y = data.target
X = df.values
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=0)

###### implemented model trial
model1 = LogisticRegression_imp(lr=0.0015,n_iter=100000)
model1.fit(X_train,y_train)
prediction1 = model1.predict(X_test)
acc1 = model1.score(y_test)

####### sklearn model trial
model2 = LogisticRegression()
model2.fit(X_train,y_train)
prediction2 = model2.predict(X_test)
acc2 = model2.score(X_test,y_test)

######printing comparison
print("-"*60)
print(f"implemented Logistic Regression model accuracy: {acc1*100}%")
print("-"*60)
print(f"sklearn's built-in Logistic Regression model accuracy: {acc2*100}%")
print("-"*60)