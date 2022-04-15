
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

print(a)

np.size(a)

np.shape(a)
print(a.dtype)
a=np.array([[2,4],[6,10]])

print(a[0][1])

s=np.arange(1,10,1)

print(s[2:5])

b=np.copy(s)

print(b)

c=np.array([[2,3,4],[5,7,8]])

print(c)

b=np.copy(c)

print(c,b)

d=b.view()

print(d)

print("a=",c)
print("b=",b)
print("c=",d)

c[0][1]=200

print(c)

print(b)


b[0][2]=1000


print(d)


np.sort(b, axis=0)

np.sort(b, axis=1)


d=np.dtype([('name','S1'),('perc','int')])

marks=np.array([('hari',20),('raju',80),('ravi',50)],dtype=d)

print(marks)
np.sort(marks,order='name')
a=np.array([[2,5],[4,10]])

b=np.array([[1,3],[6,9]])

print(np.append(a,b))

print(np.insert(a,3,20)) #array,index,elements
print(np.delete(a,3))
print(np.concatenate((a,b),axis=1))

print(a,b)

print(np.concatenate((a,b),axis=0))

print(np.stack((a,b)))

print(np.stack((a,b),axis=1))

print(np.vstack((a,b)))

print(np.hstack((a,b)))

print(a)

print(b)

print(np.dstack((a,b)))


x=np.arange(10,100,10)

print(x)

s1,s2,s3=np.split(x,3)

print(s1)


d=np.arange(10,130,10)

print(np.split(d,(2,6)))

m=np.arange(10,130,10).reshape(4,3)


print(np.where(m==80))


c=np.arange(10,100,10)
print(c)
r=np.where(c==20)

print(r)

print(np.where(c%20==0))

q=np.array([10,20,40,30,5])

print(q)

print(np.searchsorted(q,10))

print(np.searchsorted(q,[20,40,30]))

a=np.array([[2,3,4],[10,11,12]])
b=np.array([[5,6,7],[13,14,15]])

print(np.add(a,b))


print(np.subtract(a,b))

print(np.multiply(a,b))

print(np.divide(a,b))


print(np.exp(a))

print(np.sqrt(a))

print(c=a=np.array([[2,3,4],[10,11,12]]))

print(np.array_equal(a,c))

print(a==b)

print(np.min(a))

print(np.min(a,axis=1))

print(np.max(a,axis=0))
print(np.sum(a))

print(a)

print(np.sum(a,axis=0))

print(np.sum(a,axis=1))


# medain
print(np.median(a,axis=0))

print(np.var(a))

# mean
print(np.mean(a))

print(np.var(a,axis=0))

print(np.linspace(0,2,9))
