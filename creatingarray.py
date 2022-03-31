#!/usr/bin/env python
# coding: utf-8


import numpy as np


a=[[2,3],[4,6]]
b=np.asarray(a,order='F')

print(b)

for i in np.nditer(b):
  print(i)

a=np.zeros([2,3])

print(a)

b=np.full([2,3,3],10)

print(b)

c=np.ones([2,3])


print(c)

x=np.random.rand(2,4,4)


print(x)

c=np.eye(4)

print(c)



y=np.arange(10,20,3)



print(y)

a=np.arange(1,11,1)


print(a)

a.reshape(2,5)



c=np.linspace(10,20,10,endpoint=False,retstep=True,dtype=int)

print(c)

d=np.logspace(1,20,10,base=2)


print(d)

a=np.arange(1,10,1)

print(a)


a=a.reshape(3,3)


# In[ ]:


print(a)


# In[ ]:


np.size(a)


# In[ ]:


np.shape(a)


# In[ ]:


a.dtype


# In[ ]:


a=np.array([[2,4],[6,10]])


# In[ ]:


a[0][1]


# In[ ]:


s=np.arange(1,10,1)


# In[ ]:


s[2:5]


# In[ ]:


b=np.copy(s)


# In[ ]:


print(b)


# In[ ]:


c=np.array([[2,3,4],[5,7,8]])


# In[ ]:


print(c)


# In[ ]:


b=np.copy(c)


# In[ ]:


c,b


# In[ ]:


d=b.view()


# In[ ]:


print(d)


# In[ ]:


print("a=",c)
print("b=",b)
print("c=",d)


# In[ ]:


c[0][1]=200


# In[ ]:


print(c)


# In[ ]:


print(b)


# In[ ]:


b[0][2]=1000


# In[ ]:


print(d)


# In[ ]:


np.sort(b, axis=0)


# In[ ]:


np.sort(b, axis=1)


# In[ ]:


d=np.dtype([('name','S1'),('perc','int')])


# In[ ]:



marks=np.array([('hari',20),('raju',80),('ravi',50)],dtype=d)


# In[ ]:


print(marks)


# In[ ]:


np.sort(marks,order='name')


# In[ ]:


a=np.array([[2,5],[4,10]])


# In[ ]:


b=np.array([[1,3],[6,9]])


# In[ ]:


np.append(a,b)


# In[ ]:


np.insert(a,3,20)  #array,index,elements


# In[ ]:


np.delete(a,3)


# In[ ]:


np.concatenate((a,b),axis=1)


# In[ ]:


a,b


# In[ ]:


np.concatenate((a,b),axis=0)


# In[ ]:


np.stack((a,b))


# In[ ]:


np.stack((a,b),axis=1)


# In[ ]:


np.vstack((a,b))


# In[ ]:


np.hstack((a,b))


# In[ ]:


a


# In[ ]:


b


# In[ ]:


np.dstack((a,b))


# In[ ]:


x=np.arange(10,100,10)


# In[ ]:


print(x)


# In[ ]:


s1,s2,s3=np.split(x,3)


# In[ ]:


print(s1)


# In[ ]:


d=np.arange(10,130,10)


# In[ ]:


np.split(d,(2,6))


# In[ ]:


m=np.arange(10,130,10).reshape(4,3)


# In[ ]:


np.where(m==80)


# In[ ]:


c=np.arange(10,100,10)


# In[ ]:


r=np.where(c==20)


# In[ ]:


print(r)


# In[ ]:


np.where(c%20==0)


# In[ ]:


q=np.array([10,20,40,30,5])


# In[ ]:


print(q)


# In[ ]:


np.searchsorted(q,10)


# In[ ]:


np.searchsorted(q,[20,40,30])


# In[ ]:


a=np.array([[2,3,4],[10,11,12]])
b=np.array([[5,6,7],[13,14,15]])


# In[ ]:


np.add(a,b)


# In[ ]:


np.subtract(a,b)


# In[ ]:


np.multiply(a,b)


# In[ ]:


np.divide(a,b)


# In[ ]:


np.exp(a)


# In[ ]:


np.sqrt(a)


# In[ ]:


c=a=np.array([[2,3,4],[10,11,12]])


# In[ ]:


np.array_equal(a,c)


# In[ ]:


a==b


# In[ ]:


np.min(a)


# In[ ]:


np.min(a,axis=1)


# In[ ]:


np.max(a,axis=0)


# In[ ]:


np.sum(a)


# In[ ]:


a


# In[ ]:


np.sum(a,axis=0)


# In[ ]:


np.sum(a,axis=1)


# In[ ]:


np.median(a,axis=0)


# In[ ]:


np.var(a)


# In[ ]:


np.mean(a)


# In[ ]:


np.var(a,axis=0)


# In[3]:


np.linspace(0,2,9)

