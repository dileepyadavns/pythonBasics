#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Content Copyright by Pierian Data</em></center>

# # Statements Assessment Test
# Let's test your knowledge!

# _____
# **Use <code>for</code>, .split(), and <code>if</code> to create a Statement that will print out words that start with 's':**

# In[4]:


st = 'Print only the words that start with s in this sentence'


# In[5]:


for i in st.split():
    if i[0]=='s':
        print(i)


# In[ ]:





# In[ ]:





# ______
# **Use range() to print all the even numbers from 0 to 10.**

# In[ ]:


for i in range(0,10):
    if i%2==0:
        print(i)


# ___
# **Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.**

# In[6]:


#Code in this cell
myli=[x for x in range(1,50) if x%3==0]


# In[7]:


myli


# In[ ]:





# _____
# **Go through the string below and if the length of a word is even print "even!"**

# In[ ]:


st = 'Print every word in this sentence that has an even number of letters'


# In[15]:


for i in st.split():
    if len(i)%2==0:
        print('even!')


# In[ ]:





# ____
# **Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".**

# In[14]:


for i in range(1,100):
    if (i%3==0) and (i%5==0):
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    elif  i%3==0: 
        print("FizzBuzz")


# ____
# **Use List Comprehension to create a list of the first letters of every word in the string below:**

# In[ ]:


st = 'Create a list of the first letters of every word in this string'


# In[20]:


#Code in this cell
string=[i[0] for i in st.split()]
print(string)


# ### Great Job!
