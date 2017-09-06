from __future__ import division
import numpy as np

# user defines function, staring and end points, and chunk number
begin = float(raw_input("Staring Val:  "))
end = float( raw_input("Final Val:  "))
chunk = int(raw_input("Chunk Number:  "))

def riemannsum(func, a, b, N):
    i = 1
    sum = 0
    width = (b-a)/N
    for i in range(0 , N):
       sum = sum + func(a+i*width)*width
       i = i +1
    print  sum

def quadratic(x):
    return x**2 + 2

riemannsum(quadratic,begin,end,chunk)
    
#Implement the Riemann Sum approximation for integrals.
