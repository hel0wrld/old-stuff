import numpy as np
from scipy.stats import multivariate_normal
import pandas as pd

class GDA:
    #Finding the necessary parameters, phi, mean and covariance matrix
    #Storing the mean in array eliminates the problem of handling two variables for two distinct classes
    #This has been done by generalizing the number of means by storing it as 'n_classes'
    def CalcParameters(self, X, y):
        #Finding the number of samples and features
        n_samples, n_features = X.shape
        self.classes = np.unique(y)
        n_classes = len(self.classes)
        
        #Initializing the phi, mean and covariance variables according to the size 
        self.phi = np.zeros((n_classes, 1))
        self.mean = np.zeros((n_classes, n_features))
        self.covariance = 0
        for i in range(n_classes):
            indexes = np.flatnonzero(y == self.classes[i])                  #Only collecting the indices where y==1
            self.phi[i] = len(indexes) / n_samples                          #Finding the mean using those indices 
            self.mean[i] = np.mean(X[indexes], axis=0)                      #Finding the mean of this particular class
            self.covariance += np.cov(X[indexes].T) * (len(indexes) - 1) 

        self.covariance /= n_samples                                        #Finding the covariance

    def predict(self, X):
        pdf = lambda mean: multivariate_normal.pdf(X, mean=mean, cov=self.covariance) #Finding the probabilty distribution value using mean and covariance obtained
        y_probs = np.apply_along_axis(pdf, 1, self.mean) * self.phi                   #Applying the prob. dist. fn. to each of the entries in mean matrix
                                                                                      #Then multiplying it with phi to get the complete probability
        return self.classes[np.argmax(y_probs, axis=0)]

data = ['ds1_test.csv', 'ds1_train.csv', 'ds2_test.csv', 'ds2_train.csv'] 
for sample in data:
    print('Making a model for',sample)
    dataset = pd.read_csv(sample).to_numpy()
    x = dataset[:,:2]
    y = dataset[:, 2]
    model = GDA()
    model.CalcParameters(x, y)
    result = model.predict(x)
    print('Model made successfully')
    print('Accuracy = ',(sum(y==result)/y.shape[0]))