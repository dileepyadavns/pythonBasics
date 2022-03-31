




# **Polymorphisam**


class Cat():
  def __init__(self,name):
    self.name=name
  def speak(self):
   return self.name + " says Meow!"   


# In[87]:


class Dog():
  def __init__(self,name):
    self.name=name
  def speak(self):
   return self.name + " says woof!"   



my_dog=Dog("niko")
my_cat=Cat("felix")




for pet in (my_dog,my_cat):
  print(pet.speak())



class Animal():
  def __init__(self,name):
    self.name=name
  def speak(self):
    raise NotImplementedError("subclass must implememt this abstract method")  



myanimal=Animal('fred')
# myanimal.speak() #Abstract Method this cant we  implemented from parent class


class Cat():
  def __init__(self,name):
    self.name=name
  def speak(self):
    return self.name +" can say Meow!"




mycat=Cat("felix")
print(mycat.speak())




class Dog():
  def __init__(self,name):
    self.name=name
  def speak(self):
    return self.name +" can say woooh!"




mydog=Dog("fred")
print(mydog.speak())


# **Magic methods**

class Dog():
  def __init__(self,name):
    self.name=name
  def speak(self):
    return self.name +" can say woooh!"

  def __str__(self):
    return "string is appeared"  



c=Dog("fred")

print(c)


c.__str__()
