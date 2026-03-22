#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from numpy import sin, cos, exp, pi
from scipy.integrate import quad

def evaluation(func, x):

    try:
        allowed = {"x": x, "sin": sin, "cos": cos, "exp": exp, "pi": pi}
        return eval(func, allowed)
    except NameError:
        print("Unknown function or variable used.")
    except SyntaxError:
        print("The expression is not mathematically valid.")
    except Exception:
        print("An unexpected error occurred.")
        return None

def montepython(func, a, b, n=100000):
    try:
        x = np.random.uniform(a, b, n)
        allowed = {"x": x, "sin": sin, "cos": cos, "exp": exp, "pi": pi}
        y = eval(func, allowed)
        integral = (b-a)*np.mean(y)
        return integral 
    except Exception:
        print('Monte Carlo Integration Error')
        return None
        
lower, upper = 0, pi
input_function = input("Enter F(x): ")

test = 1
first_eval = evaluation(input_function, test)
    
mc = montepython(input_function, lower, upper)
        
print(f"Monte Carlo Integration: {mc}")
print(f"First Evaluation at {test}: {first_eval}")

