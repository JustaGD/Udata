
# coding: utf-8

# In[73]:


import pandas as pd
import numpy as np
from collections import defaultdict
from scipy.stats import hmean
from scipy.spatial.distance import cdist
from scipy import stats
import numbers
from sklearn.linear_model import LinearRegression


# In[74]:


def drop_na(df, axis = 'row'):
        row = set([])
        cols = set([])
        for col in df.columns:
            for i in range(len(df[col])):
                if pd.isnull(df.loc[i, col]):
                    row.add(i)
                    cols.add(col)
        if axis == 'row':
            df = df.drop(row, axis = 0)
        else:
            df = df.drop(cols, axis = 1)
        df.index = list(range(df.shape[0]))
        return df
  

# In[75]:

def fill_na(data, fill = 'mean'):
        data = pd.DataFrame(data)
        for col in data.columns:
            if fill == 'mean':
                tmp = data[col].mean()
            if fill =='median':
                tmp = data[col].median()
            if fill == 'mode':
                tmp = data[col].mode()[0]
            for i in range(len(data[col])):
                if pd.isnull(data.loc[i, col]):
                    ch = ch + 1
                    data.loc[i, col] = tmp
        return data


# In[8]:


def normal(data):
    data = pd.DataFrame(data)
    for col in data.columns:
        data[col] = (data[col] - data[col].mean())/data[col].std()
    return data
   


# In[9]:


def scal(data):
    
    data = pd.DataFrame(data)
    for col in data.columns:
        data[col] = (data[col] - data[col].min())/(data[col].max() - data[col].min())
    return data



