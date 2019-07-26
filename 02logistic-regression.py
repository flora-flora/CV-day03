
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

def model(theta,X):
    z=np.sum(theta.T*X,axis=1)
    return sigmoid(z)

def cross_entropy(y,y_hat):
    return sum(-y*np.log(y_hat)-(1-y)*np.log(1-y_hat))/n

def cost(theta,X,y):
    y_hat=model(theta,X);
    return cross_entropy(y,y_hat)

def optimize(theta,X,y):
    n = X.shape[0]
    alpha=1e-1
    y_hat = model(theta,X)
    dtheta = 1.0/n * ((y_hat-y)*X)
    dtheta = np.sum(dtheta,axis=0)
    theta=theta-alpha*dtheta
    return theta


def predict(theta,X):
    y_hat = model(theta,X)
    y_hard = (y_hat>0.5)*1;
    return y_hard

def accuracy(theta,X,y):
    y_hard = predict(theta,X);
    count = sum(y_hard==y)
    return count*1.0/len(y)


# k是优化次数
def loop(theta,X,y,k):
    costs=[]
    accs=[]
    for i in range (k):
        theta=optimizeoptimize(theta,X,y)
    costs.append(cost(theta,X,y))
    accs.append(accuracy(theta,X,y))
    return theta,costs,accs

