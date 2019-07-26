
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# a、b权重，x输入，y输出，n样本的总数量
def model(a,b,x):
    return a*x+b

def cost_f(a,b,x,y,n):
    return 0.5/n * (np.square(a*x+b-y)).sum()

def optimize(a,b,x,y,n):
    alpha=1e-1
    y_hat = model(a,b,x)
    da = 1.0/n * ((y_hat-y)*x).sum()
    db = 1.0/n * (y_hat-y).sum()
    a = a - alpha*da
    b = b - alpha*db
    return a,b

# k是优化次数
def loop(a,b,x,y,n,k):
    for i in range (k):
        a,b=optimize(a,b,x,y,n)
    y_hat = model(a,b,x)
    cost = cost_f(a,b,x,y,n)
    print(a,b,cost)
    plt.scatter(x,y)
    plt.plot(x,y_hat)
    return a,b

loop(0,0,x,y,100,1000)

