#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
from datetime import datetime

# In[5]:


d_parser = lambda x: datetime.strptime(x, '%Y-%m-%d')
 # we can aslo add here to parse date df=pd.read_csv("/content/1inch.csv",parse-dates=df['Date'],date_parser=dateParser)
df = pd.read_csv('1inch.csv' ,parse_dates=['Date'], date_parser=d_parser)


# In[6]:


print(df.head())


# In[7]:


print(df.shape)


# In[8]:


df.loc[0,"Date"]  # if it show error do dateformatting pd.t0_datetime(df['Date', format='%Y-%m-%d %I-%p'])


# In[9]:


print(df.loc[0,"Date"].day_name())


# In[10]:


df['Date']=pd.to_datetime(df['Date'])


# In[11]:


print(df['Date'].dt.day_name())


# In[12]:


df['DayofWeek']=df['Date'].dt.day_name()


# In[13]:


print(df)


# In[14]:


print(df['Date'].min())


# In[15]:


print(df['Date'].max())


# In[16]:


filt = (df['Date'] >= pd.to_datetime('2020-01-01')) & (df['Date'] < pd.to_datetime('2022-01-01'))
print(df.loc[filt])


# In[17]:


df.set_index('Date', inplace=True)


# In[18]:


print(df.head())


# In[19]:


print(df['2022'])


# In[20]:


print(df['2021-06':'2022-04'])


# In[21]:


print(df['2021-06':'2022-04']['Close'].mean())


# In[22]:


print(df['2022-01']['High'].max())


# In[23]:


high=df['High'].resample("D").max()


# In[24]:


print(high["2020-12-25"])


# In[25]:





# In[27]:


print(df.resample("w").mean())


# In[28]:



df.resample('W').agg({'Close': 'mean', 'High': 'max', 'Low': 'min', 'Volume': 'sum'})


# In[31]:


print(np.asarray(df["Open"]))






