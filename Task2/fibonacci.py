#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a = 1
b = 2
for i in range(100):
  a, b = b, a+b 
print(b)

