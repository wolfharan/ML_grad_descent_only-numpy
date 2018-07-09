from __future__ import division 
import numpy as np

def meansqrerror(weights,data):
    err=0
    for i in range(1,len(data)):
        productsum=np.dot(data[i][1:14],weights)
        err+=(data[i,-1]-productsum)**2
    return err/(len(data)-1)
    
    
def gradient(weights,data,learnrate):
    w_grad=np.zeros(13)
    N=len(data)-1
    for i in range(1,len(data)):
        for k in range(1,len(data[1])-1):
            err=(data[i,-1]-(np.dot(data[i][1:14],weights)))
            w_grad[k-1]+= -(2/N)*data[i,k]*err
    nweights = weights-(learnrate*w_grad)
    return nweights

def grad_run(weights,data,learnrate,iterations):
    mse=meansqrerror(weights,data)
    for i in range(iterations):
        weights=gradient(weights,data,learnrate)
        mse=meansqrerror(weights,data)
    return weights
