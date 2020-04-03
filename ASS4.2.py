#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df = pd.read_csv(r"C:\Users\Envy 360\Desktop\learn-data-analysis-w-python-master\learn-data-analysis-w-python-master\datasets\gradedata.csv")
df.head()


# In[3]:


import numpy as np
df['timemgmt']=np.where((df['exercise']>3)&(df['hours']>17),'busy','idle')


# In[4]:


df.tail()


# In[ ]:




