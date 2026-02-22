#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

a = float(input("Enter the value of the coefficient a:" ))
b = float(input("Enter the value of the coefficient b:"))
c = float(input("Enter the value of the coefficient c:"))

D = b*b-4*a*c

if D>0:
 x1 = (-b+math.sqrt(D))/(2*a)
 x2 = (-b-math.sqrt(D))/(2*a)
 print(f"The real solutions of the given quadratic equation are {x1} and {x2}.")
elif D==0:
 x1 = (-b)/(2*a)
 print(f"The real solution of the given quadratic equation is {x1}.")
else:
    print("This equation has no real solutions.")

