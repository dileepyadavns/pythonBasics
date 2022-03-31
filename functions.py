# in this problem 3 inputs taken from user if sum lessthan 21 will prent sum.
# else if sum greater than 21 and one number among inputs is 11 sum will be printed as sum-10
# else return bust.
def blackjack(a,b,c):
  sum1=sum([a,b,c])
  if sum1<=21:
    return sum1
  elif sum1>21 and 11 in [a,b,c]:
    sum1=sum1-10
    return sum1
  else:
    return 'BUST'

a=int(input())
b=int(input())
c=int(input())
print(blackjack(a,b,c))

# print sum of numbers in list excluding numbers between 6 and 9 using enemerate:

def sum_of_numbers(list_a):
  sum1=0
  for a,i in enumerate(list_a):
    if i=='6':
       
        if ('9' in list_a[a+1:]):
          index1=int(list_a.index('9'))
         
        else:
            return list_a[:a]+[0]
        return list_a[:a]+list_a[index1+1:]
        break
       


list_a=input().split()
list_b=sum_of_numbers(list_a)
sum1=0
for i in list_b:
  sum1+=int(i)
print(sum1)  

# print sum of numbers in list excluding numbers between 6 and 9 using while loop:


def sum_of_numbers(list_a):
  add=True
  sum1=0
  for i in list_a:
    while add:
      if i!=6:
        sum1+=i
        break
      else:
        add=False
    while not add:
      if i!=9:
        break
      else:
        add=True
        break
  return sum1 
print(sum_of_numbers([1,2,6,2,2,2,9,1]))            

# checking whether the list taken from inputt follows order [0,0,7]

def order_follows(list_a):
  code=[0,0,7,'x']

  for i in list_a:
    if i==code[0]:
      code.pop(0)
  return len(code)==1
print(order_follows([1,2,0,2,3,0,7,8]))    
print(order_follows([1,2,7,2,3,0,0,8])) 

