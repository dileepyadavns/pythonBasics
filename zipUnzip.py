#!/usr/bin/env python
# coding: utf-8

# In[16]:


from datetime  import datetime
from datetime import timedelta


# In[21]:


t2=timedelta(days=345,minutes=20)


# In[22]:


t2.days


# In[3]:


fil1=open('file1.txt','w+')
fil1.write("hi dileep")


# In[4]:


fil2=open('file2.txt','w+')
fil2.write("hey golla")


# In[22]:


import zipfile
comprfile=zipfile.ZipFile('comprfile.zip','w')


# In[23]:


comprfile.write('file1.txt',compress_type=zipfile.ZIP_DEFLATED)


# In[24]:


comprfile.write('file2.txt',compress_type=zipfile.ZIP_DEFLATED)


# In[25]:


zip_obj=zipfile.ZipFile('comprfile.zip','r')


# In[26]:


zip_obj.extractall("extracted")

