
from __future__ import division 
from implementation import *
import numpy as np

data = np.genfromtxt('train.csv', delimiter=',',dtype=np.float64)
weights=np.array([1,1,1,1,1,1,1,1,1,1,1,1,1])
weights=grad_run(weights,data,0.000001,50000)
print(weights)
print(meansqrerror(weights,data))
