
import numpy as np #importing library


a=np.array([1,34,5])
print(a)


b=np.array(56) # Zero Dimensional Array 

c=np.array([1,2,3]) # array of 0D Elements is 1D Array

d=np.array([[1,2,3],[10,12,15]]) #Array of 1D elements is 2D Array

e=np.array([[[1,2,3],[10,12,15]],[[1,4,3],[10,10,15]]])

#To find the dimensions of Array
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print(e.ndim)
print(type(e))


# Creation of Existing Array
# np.asarray(input.dtype,order) "C=row major order,"F"=Column major order

l=[1,2,3]
a=np.asarray(l,float,"C")
print(a)

l=[[1,2,3],[6,7,2]]
b=np.asarray(l,dtype=float,order="F")
print(b)


for i in np.nditer(b):
  print(i)     # by printing the each value u will come to which order it is followingh 


b=np.asarray(l,dtype=float,order="C")
print(b)

for i in np.nditer(b):
  print(i)
m=b"dillep"
c=np.frombuffer(m, dtype="S1", count=-1,offset=0)
print(c)

m=b"dillep"
c=np.frombuffer(m, dtype="S1", count=-1,offset=3)
print(c)


m=b"dillep"
c=np.frombuffer(m, dtype="S1", count=5,offset=0)  # given count as 5
print(c)
m='dileep'

c=np.fromiter(m,dtype='S1')
print(c)

m=[1,2,3]
c=np.fromiter(m,dtype='float',count=-1)
print(c)


# Arange,linespace,logspace

print(np.arange(1,10,2,int))
print(np.arange(1,10,2,float))
print(np.linspace(1,20,20,True,True))  #linspace(start,stop,num,endpoint,retstep,dtype)  => 'num is the number of values betweeen intervals default=50

                       # 'endpoint=>true or false which is whether to include stopindex or not. default=True
 
                       # 'retstep' => difference between the elements (True/False) default value False

                       #'dtype'=> float/int 



print(np.linspace(1,20,20,endpoint=False,retstep=True))
print(np.logspace(1,20,20,base=2,endpoint=True)) ##logspace(start,stop,num,endpoint,base,dtype)

# zeros,full,ones,eye
print(np.shape(a))
print(b.shape)
print(np.zeros((2,4),dtype=int))
print(np.ones((3,3),dtype=int))
print(np.full((5,5),50)) #full(shape, num)=> num is the elemntwe want in array
print(np.eye(6))  #np.eye(rows/colums) rows=colums

a=[1,1,2,3,4,5,6,8,9]
print(np.reshape(a,(3,3)))
print(np.reshape(a,(9,1)))


# Accessing & Slicing

e=np.array([[[1,2,3],[10,12,15]],[[1,4,3],[10,10,15]]])
d=np.array([[1,2,3],[10,12,15]])
c=np.array([1,2,3])
print(e[0][0][2])
print(e[0][1][-1])
print(e[0,1,-1])
print(e[0,0,2])
print(d[0,2])
print(e[-1,-1,-1])
print(a[::])
print(a)
print(a[:5:2])


d=np.array([[1,2,3],[10,12,15]])
print(d[1,1])
print(d[0:2,0:2])

e=np.array([[[1,2,3],[10,12,15]],[[1,4,3],[10,10,15]]])
print(e[1,1,:2])
print(e[:2,:2,:2])


d=[[10,2,12],[5,30,20]]
print(np.sort(d,axis=1))
print(np.sort(d,axis=0))

print(e)
print(np.sort(e,axis=1))

x=np.sort(e,axis=0)
print(x)
print(x.dtype)
print(x.astype("f")) #converted to float data type


# Copy and View
#copy creates an external array if element changed in array then the elements doesnt get changed
# in the copy array where as in view the changes will get reflected

print(x)
b=x.copy()
c=x.view()
x[0][0][0]=100
print(x)
print(b)
print(c)


a=np.array([1,2,3,10,8,20],dtype='f')
print(a)

l=a.copy()
m=a.view()
a[0]=2000.0
print(l)
print(m)


b=a.astype("U")
print(b.dtype)


c=a.astype(bool)
print(c)
print(c.dtype)

a=np.array([[3,4,5],[10,20,5]])
b=np.array([[11,0,6],[100,20,50]])
print(a)
print(b)

print(np.concatenate((a,b))) #parameters should be placed in tuple
print(np.concatenate((a,b),axis=1))
print(np.stack((a,b)))  # stack will form an array with each array as element
print(np.stack((a,b) ,axis=1))
print(np.stack((a,b),axis=0))
print(np.hstack((a,b))) #it is like row conactente (axis=1)
print(np.vstack((a,b))) #like column concatenate axis=0
print(np.dstack((a,b))) #take each element from each array and make a rows a forming new array


a=np.arange(1,10)
print(a[::-1])
print(a*10)
print(a/2)
print(np.split(a,3)) #it will split into equal divisions if not possible will show error
print(np.array_split(a,2))#it will arrange into arrays though it doesnt have equal  divsions it will divide

d=np.array([[1,2,3],[10,12,15]])
print(d)
print(np.vsplit(d,2)) #vsplit doesnt work on single dimensions
print(np.hsplit(d,3)) # cannot work with equal division
print(np.vsplit(d,2))

print(a)
print(np.where(a%2==0))#where return the index of the given value  

#Searched Sort =>returns the index where the specified value should be inserted.
#Elements should be in sorted order before implementing searchsorted
a=[1,10,3,5,8,7]
a=np.asarray(a)
a=np.sort(a)
print(a)
print(np.searchsorted(a,2))
print(np.searchsorted(a,[2,4,6,9,11])) 


m=np.array([[30,20,40],[10,300,25]])
print(np.sort(m,axis=0)) #sort(array,axis,order,kind) kind as merge sort and quick sort
print(np.sort(m,axis=1))

d=np.dtype([('name',"S1"),("Percent", float)])
x=np.array([('abc',60.5),("Arun",90.25),('Abhi',87.5)], dtype=d)
print(np.sort(x,order="Percent"))
print(np.sort(x,order='name'))


