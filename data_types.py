
list1=['hi','dileep']
list2=['two','one']

print(list1+list2)

list1[0]='Hello'

print(list1)
 
#adds element at the end of list

list1.append("golla")

print(list1)

# removes last element from list
list1.pop()

print(list1)

# removes element from index 0
list1.pop(0)

print(list1)

listo=[1,7,3,8,2]


# sorts the elements in ascending order by default
listo.sort()

print(listo)

# reverses the elements in the list
listo.reverse()


print(listo)

# Dictionary 

my_dict={'apple':20,'mango':100,'orange':50,'grapes':200}


print(my_dict['apple'])


d2={'k1':{'apple':20,'mango':100,'orange':50,'grapes':200},'p1':200,'ro':29}

# acessing a key from dictionary
print(d2['k1'])



d3={'p1':[10,2,4,6]}


d3['p1'][2]

# returns list of all keys in dictionary

d2.keys()

# returns list of value.
d2.values()
# returns list containing tuple with key and value.

d2.items()


# return tuple
print(type((1,)))

#returns int
type((1))

# tuples

#creating a tuple
new=() 

print(type(new))


t=('1','1',3,4)


print(t.count('1'))


print(list1)

list1[0]='gdy'


print(list1)

# t[0]=3 tuple doesnt support assingment as tuple is immutable

#sets

myset=set() #creating set


print(myset)


myset.add(1) # adds elemet into set



print(myset)



myset.add(1)
# set cannt add duplicates

print(myset)

tu=()

print(type(tu))

mylist3=[1,1,2,3,4,4,4,5,6,6,7]



print(set(mylist3)) # convert list to set



b=None #none data type


print(b)


print(type(b))


list12=[1,2,3,4,5,6,7,8,9,10]


for i in list12:
    if i%2==0:
        print("evenNUmber: {} ".format(i))



myl=[(1,3),(5,7),(9,11),(13,15)]


for a,b in myl:
    print(a)
    print(b)



print(my_dict)


for items in my_dict:
    print(items)


for items in my_dict.items():
    print(items)


for keys,val in my_dict.items():
    print(val)


for _ in "hell":
    print('cool')


ic=0

for i in 'abcde':
    print('{} is at {}'.format(i,ic))
    ic+=1



for a,b in enumerate("abcdef"):
    print('{} is at {} '.format(a,b))



my1=[1,2,3,4]
my2=['one','two','thre','four']
my3=['a','b','c']



zipped=zip(my1,my2,my3)

print(zipped)

for item in  zipped:
    print(item)



from random import shuffle


mylist=[1,2,3,4,5]


shuffle(mylist)


print(mylist)



print(type(shuffle(mylist)))


from random import randint

print(randint(0,100))


#Even Check in a List:

def even_check(list_a):
    for i in list_a:
        if i%2==0:
            return True
        else:
            pass
    return False   
            

print(even_check([1,2,3]))


def print_even(list_a):
    new=[]
    for i in list_a:
        if i%2==0:
            new.append(i)
        else:
            pass
    return new   


print(print_even([1,2,3,4]))


print(print_even([1,3,5]))


#Employ of the Month

def employee_month(list_a):
    current_max=0
    employee_month=''
    for name,whrs in list_a:
        if whrs>current_max:
            current_max=whrs
            employee_month=name
        else:
            pass
    return(employee_month,current_max)

 
print(employee_month([('dileep',200),('arjun',500),('vikas',1000)]))


name,hrs=employee_month([('dileep',200),('arjun',500),('vikas',1000)])


print(name)



print(hrs)


#Guess Game

from random import shuffle


def shuffled_list(my_list):
    shuffle(my_list)
    return my_list

def user_guess():
    guess=''
    
    while guess not in ['0','1','2']:
        guess=input()
    return int(guess)    


def check_guess(example,guess):
    if example[guess]=="O":
        print("Guess is Correct")
        print(example)
    else:    
        print("Incorrect Guess")
        print(example)


my_list=[' ',' ','O']
list1=shuffled_list(my_list)
print(list1)



list2=int(user_guess())



check_guess(example=list1,guess=list2,)



for a,b in enumerate('abcd'):
    print(a)


list1=['dileep','shubham']



new=[]
for i in list1:
    
    new.append(i[:3]+i[5:])
print(new)    
      


list1=['dileep','shubham']


new=[]
for i in list1:
    if i=='dileep':
        i=list1[0].replace('dileep','dlp')
    new.append(i)    
print(new)    


li1=[1,2,3,4]
print(list(map(lambda a:a**2,li1)))


print(list(filter(lambda a:a%2==0,li1)))


from functools import reduce

print(reduce(lambda a,b : a*b,li1))

num=[1,2,3,4,5,6,7]
evens=list(filter(lambda n : n%2==0,num))
print(evens)






