# -*- coding: utf-8 -*-
"""Polynomial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R7J8Gpxrs8fDdBe4Dyx3d1M4-A0Lb47z
"""

from math import exp as e
from math import cos as cos
import math
from sympy import *
from math import *
from __future__ import division
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange

fx = '(exp(x) + 2**-x+ 2*cos(x) - 6)'
f= lambda x: eval(fx)
interval_start= input("enter starting point: ")
interval_end= input("enter ending point: ")
n= int(input("enter n: "))
x=[]
y_values=[]
difference= (int(interval_end) - int(interval_start))/int(n)
for i in range(n+1):
  x.append(int(interval_start) + i*difference)
for i in x:
  y_values.append(f(i))

poly = lagrange(x, y_values)
lang_vals=poly(x)
E=y_values-lang_vals
plt.plot(x,lang_vals, 'bo-', label='Langrange')
plt.plot(x,y_values,'gs-',  label='F(x)')
plt.plot(x,E,'ro-',  label='error')
plt.title("Langrange Plot")
plt.xlabel("X values")
plt.ylabel("F(x)")
plt.show()

