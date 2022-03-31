#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


df=pd.read_excel("multi_threading_activity.xlsx")


# In[ ]:


print(df)


# In[ ]:


df.value_counts()


# In[ ]:


df["B"]=pd.to_numeric(df["B"], errors="coerce")


# In[ ]:


df["A"]=pd.to_numeric(df["A"], errors="coerce")


# In[ ]:


df.replace("NaN",0)


# In[ ]:


df['sub']=df['A']-df['B']


# In[ ]:


df


# In[ ]:


dict={ "A":[1,2,3,5,6],"B":[10,20,30,40,50],"C":[400,400,500,600,300]}


# In[ ]:


df2=pd.DataFrame(dict)


# In[ ]:


print(df2)


# In[ ]:


df2['sum2']=df2['A']+df2['B']+df2['C']


# In[ ]:


print(df2)


# In[ ]:


df.values.tolist()


# In[ ]:


persons={
    'first':['dileep','arjun','vikas','krishna'],
    'last':['golla','boddu','vatte','golla'],
     'study':['Btech','Degree','Tenth',"Inter"],
     'place':['suryapet','hyderabad','kodad','suryapet']
}


# In[ ]:


df1=pd.DataFrame(persons)


# In[ ]:




