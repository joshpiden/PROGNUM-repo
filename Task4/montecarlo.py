#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def montepython(func_str, a, b, n = 10000):

    x = np.random.uniform(a, b, n)

    y = eval(func_str)

    integral = (b-a)*np.mean(y)
    return integral

func = input("Here be function:")
a = float(input("Here be lower:"))
b = float(input("Here be upper:")) 

result = montepython(func, a, b)

print(result)

