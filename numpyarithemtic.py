import numpy as np

#arithemetic operaions
a=np.array([[2,3,3],[4,5,10],[2,2,2]])
b=np.array([[1,4,5],[0,7,18],[1,5,5]])

print(np.add(a,b))

print(np.subtract(a,b))

print(np.multiply(a,b))


print(np.divide(a,b))

c=np.array([10,10,20])


print(np.add(a,c))



d=np.array([10,50])

print(a)


print(c)


print(np.divide(a,c))

print(np.multiply(a,c))


print(np.reciprocal(a)) #it will return only integers


print(np.mod(a,2))


print(np.power(a,b))

print(np.power(a,2))


c=[5.0+6.j,2.+1.j,10.+2.j]


print(np.real(c))

print(np.imag(c))

print(np.conjugate(c))


print(a)



print(np.amin(a))


print(np.amin(a,axis=0))


print(np.amax(a,axis=1))

print(np.average(a))

print(np.mean(a))

w1=[1,2,3]


# In[158]:


print(np.average(a,weights=w1,axis=0)) #weighted average

print(np.mean(a,axis=0))

print(a)


# In[161]:


print(np.median(a))

print(np.median(a,axis=0))

print(np.median(a,axis=1))


print(np.var(a))



print(np.std(a))

print(a)


print(np.sort(a,kind= "mergesort"))


# In[170]:


print(np.sort(a))
