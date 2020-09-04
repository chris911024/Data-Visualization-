#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np 
import matplotlib.pyplot as plt
x = np.linspace(0,10,30)
y = np.sin(x)
plt.plot(x,y,'o',color = 'b')
plt.plot(x, y, '-p', color='g',
        markersize=15, linewidth=4, 
        markerfacecolor='white', markeredgecolor='r',
        markeredgewidth=2)
plt.ylim(-1.2, 1.2)


# In[ ]:




