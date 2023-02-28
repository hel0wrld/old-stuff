import numpy as np
import pandas as pd

class GDA:
    
    def parameters(self, x, y, X, Y):
        phi = np.mean(y==1)
        indices = [y == 0]
        dr = len(indices)
        num = np.sum(x[indices], axis=1)
        mu_0 = num/dr
        indices = [y==1]
        num = np.sum(x[indices], axis=1)
        dr = len(indices)
        mu_1 = num/dr
        print(phi, mu_0, mu_1)

        mu = [mu_0, mu_1]
        x_minus_mu = x[0] - mu[0]
        x_minus_mu = x_minus_mu.reshape(*(x_minus_mu.shape), 1)
        s = np.matmul(x_minus_mu, x_minus_mu.T)

        m = len(y)

        for i in range(1, m):
            x_minus_mu = x[i] - mu[i]
            x_minus_mu = x_minus_mu.reshape(*(x_minus_mu.shape), 1)
            s += np.matmul(x_minus_mu, x_minus_mu.T)
 
        s /= m

        pi = 3.1415926535
        n = len(mu_0) # Or mu_1, or any of the X
        denominator = (2 * pi) ** (n / 2) * np.sqrt(np.linalg.det(s))
        
        predictions = []
        
        for x in X:
            x_minus_mu0 = x - mu_0
            x_minus_mu0 = x_minus_mu0.reshape(*(x_minus_mu0.shape), 1)
            p_x0 = 1 / denominator * np.exp(-0.5 * np.matmul(x_minus_mu0.T, np.matmul(np.linalg.inv(s), x_minus_mu0)))
            p_x0 = np.squeeze(p_x0)
        
            x_minus_mu1 = x - mu_1
            x_minus_mu1 = x_minus_mu1.reshape(*(x_minus_mu1.shape), 1)
            p_x1 = 1 / denominator * np.exp(-0.5 * np.matmul(x_minus_mu1.T, np.matmul(np.linalg.inv(s), x_minus_mu1)))
            p_x1 = np.squeeze(p_x1)
        
            if p_x1 >= p_x0:
                predictions.append(1)
            else:
                predictions.append(0)
        
        print(f"Accuracy = {sum(predictions==Y)/Y.shape[0]}")
        



dataset = pd.read_csv('ds1_test.csv').to_numpy()
x1 = dataset[:,:2]
y1 = dataset[:, 2]
dataset1 = pd.read_csv('ds1_train.csv').to_numpy()
x2 = dataset1[:,:2]
y2 = dataset1[:, 2]
model = GDA()
model.parameters(x1, y1, x2, y2)


    