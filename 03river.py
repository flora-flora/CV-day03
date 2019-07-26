
# coding: utf-8

# In[ ]:


import numpy as np

V1x=V1*np.cos(a1)
Vix=Vi*np.cos(ai)
ti=si/Vix
T=(si/Vi*np.cos(ai)).sum()
Viy=Vi+V*np.sin(ai)
siy=(Viy)*ti
syall=siy.sum()
# 最终
max(syall) # 在T恒定的情况下

