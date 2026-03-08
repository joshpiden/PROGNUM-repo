#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def gauss(x, A, x0, sig, z0):
    return A*np.exp(-(x-x0)**2/(2*sig**2))+z0

A = float(input("A:"))
x0 = float(input("x0:"))
sig = float(input("sigma:"))
z0 = float(input("z0:"))
bottom = float(input("bottom:"))
top = float(input("top:"))

x2 = np.linspace(-10, 10, 200)
y2 = gauss(x2, A, x0, sig, z0)

area, error = quad(gauss, bottom, top, args=(A, x0, sig, z0))
print(f"Area between {bottom} and {top} is: {area}")

plt.figure(figsize=(9, 6))
plt.plot(x2, y2, label=f"Gaussian Curve (A={A}, x0={x0}, σ={sig})", color="green")

x3 = np.linspace(bottom, top, 100)
y3 = gauss(x3, A, x0, sig, z0)
plt.fill_between(x3, y3, color="red", alpha=0.3, label=f"Integrated Area = {area}")

plt.legend()
plt.grid(True, linestyle = "--", alpha = 0.5)
plt.ylim(0, 1.5)
plt.title("Gaussian Function")
plt.show()

