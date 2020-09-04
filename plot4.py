#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np 
import matplotlib.pyplot as plt
x = np.linspace(0,10,30)
y = np.sin(x)
rng= np.random.RandomState(0) 
x= rng.randn(100) 
y= rng.randn(100) 
colors= rng.rand(100) 
sizes= 5000*rng.rand(100) 
plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='viridis')
plt.colorbar();  #顯示色調


# In[ ]:




