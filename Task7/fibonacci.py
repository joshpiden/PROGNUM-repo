#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Fibonacci: 
    """Calculates Fibonacci sequence"""
    
    def get_nth_term(self, n):
           
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b
    def get_divisible(self, n, m):
        
        divisible = []
        a, b = 0, 1
        
        for i in range(n):
            if a % m == 0:
                divisible.append(a)
            a, b = b, a+b
            
        return divisible 
    
n = 100
m = 7

fib = Fibonacci()

nth = fib.get_nth_term(n)
divlist = fib.get_divisible(n, m)

print(nth)
print(divlist)

