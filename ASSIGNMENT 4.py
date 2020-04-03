#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv(r"C:\Users\Envy 360\Desktop\learn-data-analysis-w-python-master\learn-data-analysis-w-python-master\datasets\gradedata.csv")


# In[3]:


df.head()


# In[5]:


# Create the bin dividers
bins = [0, 80, 100]
# Create names for the four groups
group_names = ['Fail', 'Pass']


# In[6]:


df['Pass/Fail'] = pd.cut(df['grade'], bins,
labels=group_names, right=False)


# In[7]:


df.head()


# In[ ]:




