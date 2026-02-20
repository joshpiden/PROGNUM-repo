#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Sirius data
# apparentMagnitude = -1.46
#  absoluteMagnitude = 1.45

# The distance is related to the magnitudes as m-M=5.Log(d/10)
# 1 Parsec = 3.26164 ly

m = input("Enter the apparent magnitude: ")
M = input("Enter the absolute magnitude: ") 

m2= float(m)
M2= float(M)

d = 10.0 * pow( 10.0, (m2-M2)/5.0 ) * 3.26164

s=f"The value of the distance modulus is {d} lightyears"

print(s)


