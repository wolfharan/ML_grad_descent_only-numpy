import numpy as np

weights=[-2.53052649e-03,  6.37799434e-02  ,5.35765498e-02 , 1.34296731e+00
,  1.12150492e+00 , 3.83153861e+00 , 3.38988833e-02 ,-4.50873449e-01,
  1.97035058e-01 ,-1.07131757e-02 ,-4.75105422e-02 , 2.16687194e-02,
 -6.72842697e-01]
data=np.genfromtxt('test.csv',delimiter=',',dtype=np.float64)
out=np.zeros((len(data),2))
for i in range(len(data)):
   out[i]=[data[i,0],np.dot(weights,data[i][1:])]
np.savetxt("output.csv", out, delimiter=",",fmt='%f')

