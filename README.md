# ML Gradient Descent from scratch in python to predict boston housing prices (libraries used: only python)
An implementation of Gradient Descent(from sratch, uses only Python and Numpy) to fit a line using Linear Regression to the boston housing data set.  It is more faster and easier to acheive with a library like TensorFlow, but this implementation uses no other library except for numpy. This helps in understanding Gradient Descent at a deeper level.

IMPORTANT NOTE: It takes some time for the function to finish all the 800000 iterations and produce the weights as an output. 

The Dataset is taken from - https://www.kaggle.com/c/boston-housing

The implementation.py file contains the functions-
  meansqaureerror(weights,data)
  gradient(weights,data,learnrate)
  grad_run(weights,data,learnrate)

In the function grad_run(weights,data,learnrate) we decide on the number of iterations the gradient() function should run.The current value is 800000.Increasing it will increase the accuracy but also increases the amount of time taken by the program to produce the weights.
The client file calls these functions with proper inputs.
The client file runs the grad_run function to produce the weights, then calculates the meansquareerror in the weights and then prints the weights and the error.
The printed weights are copied to the file test.py and run against test data. The output is written to output.csv file.


Running the program with iterations = 50000,learnrate=0.000001 takes arounf 480 seconds and produces weights with a variance =40.921564538642215
The weights mentioned in the test.py are obtained after experimenting with the iterations and learnrate. it produces a set of weights with a approx. variance = 27 
