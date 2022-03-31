
class Animal():
  def __init__(self):
    print("Animal created")
  def who_am_i(self):
    print("i am an Animal")  
  def eat(self):
    print("I am Eating")

my_obj=Animal()      

my_obj.who_am_i()


class Dog(Animal):
  def __init__(self):
    Animal.__init__(self)
    print("Dog Created")
  def who_am_i(self):  # method Overiding
    print('iam a dog')  



my_dog=Dog()




my_dog.who_am_i()

