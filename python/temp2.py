import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.special import expit
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
        x_axis = np.arange(1,iterations+1)
        y_axis = []
        #fcx = self.x[:,0]
        #fcw = np.zeros(fcx.shape[0])
        for i in range(iterations):
            sigma = self.sigmoid(self.x, self.weight)
            # if abs(avg-1)<0.000001:
            #     avg=0.9
            loss = self.loss(sigma, self.y)
            y_axis.append(loss)
            self.weight-=rate*self.gradient(self.x, sigma, self.y)
            #fcw-=rate*self.gradient(fcx, avg, self.y)
        print('Successfully fitted to data')
        plt.xlabel('Number of Iterations')
        plt.ylabel('Value of the Loss Function')
        plt.title('Loss vs Iterations')
        plt.plot(x_axis, y_axis)
        plt.show()

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
    
#Creating a model for ds1_test.csv
dataset = pd.read_csv('ds1_train.csv').to_numpy()
x = dataset[:,:1]
y = dataset[:,2]
model = LogRegression(x, y)
model.update(0.161, 5000)
prediction = model.classifier(x, 0.5)

#Printing the accuracy of our model
print(f"Accuracy = {sum(prediction==y)/y.shape[0]}")


