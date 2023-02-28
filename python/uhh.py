import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

class LogRegression:
    def __init__(self, x, y):
        self.intercept = np.ones((x.shape[0], 1))
        self.x = np.concatenate((self.intercept,x), axis=1)
        self.weight = np.zeros(self.x.shape[1])
        self.y = y
    
    #Sigmoid function to convert values to the range [0,1]
    def sigmoid(self, x, weight):
        z = np.dot(x, weight)
        val = 1/(1+np.exp(-z))
        return val

    #Loss function 
    def loss(self, h, y):
        val = -(y*np.log(h)+(1-y)*np.log(1-h)).mean()
        #print(y.shape[0])
        return val
    
    #Gradient calculator for updating the weights in each iteration
    def gradient(self, X, h, y):
        m = y.shape[0]
        val = np.dot(X.T, (h-y))/m
        return val

    #Fitting the model, i.e., updating the weights according to the losses and learning rate
    def update(self, rate, iterations):
        for i in range(iterations):
            sigma = self.sigmoid(self.x, self.weight)
            self.weight-=rate*self.gradient(self.x, sigma, self.y)
    print('Model set-up succesfully')

    #Classifier function, which classifies the data into the 2 binary states
    def classifier(self, x_new, threshold):
        x_new = np.concatenate((self.intercept,x_new), axis=1)
        result = self.sigmoid(x_new, self.weight)
        result = result>=threshold
        predictor = np.zeros(result.shape[0])
        for i in range(len(predictor)):
            if result[i]==True:
                predictor[i]=1
            else:
                continue
        
        return predictor
    
#Creating a model for ds1_train.csv
inputset = pd.read_csv('ds1_train.csv').to_numpy()
x = inputset[:,0:2]
y = inputset[:,2]
model = LogRegression(x, y)
model.update(0.161, 5000)
testset = pd.read_csv('ds1_test.csv').to_numpy()
x1 = testset[0:100,0:2]
y1 = testset[0:100,2]
prediction = model.classifier(x1, 0.5)

#Printing the accuracy of our model
print(f"Accuracy for ds1_train.csv = {sum(prediction==y1)/y1.shape[0]}")