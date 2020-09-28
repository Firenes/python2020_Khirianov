import numpy as np
import matplotlib.pyplot as plt

#x = 1      #(x**1) * 5 –– -3.9556950781492306
            #(x**15)    –– -2.4817638898168184

#x = 10     #(x**1) * 5 –– -0.6363269173039506
            #(x**15)    –– -7.267152843782081

#x = 100    #(x**1) * 5 –– -0.7240838114224049
            #(x**15)    –– -7.548996118176268

array = [1, 10, 100]

for x in array:
    base = 1 + x**2
    data = (1 / (np.e**np.sin(x+1))) / (5/4 + (x**15))

    y = np.log(data) / np.log(base)
    print(f'При х = {x}, y = {y}')


