#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import matplotlib.pyplot as plt
x = np.linspace(0,10,30)
y = np.sin(x)
plt.plot(x,y,'o',color = 'b')

