
lista=['dileep','shubham']
listb=[]
listb.append(lista[0].replace('dileep','dlp'))
listb.append(lista[1].replace('shubham','shham'))
print(listb)

new=[]
x=lambda lista : lista[0].replace('dileep','dlp')
y=lambda lista : lista[1].replace('shubham','shuam')
a=x(lista)
b=y(lista)
new.append(a)
new.append(b)

li1=[1,2,3,4]
print(list(map(lambda a:a**2,li1)))
print(list(filter(lambda a:a%2==0,li1)))


from functools import reduce
print(reduce(lambda a,b : a*b,li1))

num=[1,2,3,4,5,6,7]
evens=list(filter(lambda n : n%2==0,num))
print(evens)
