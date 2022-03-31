
myfile=open('myfile.txt','a')
myfile.write("hello i am dileep iam from suryapet i am graduted from jbiet")

myfile.close()
myfile=open('myfile.txt','r')
a=myfile.read()

print(a)
print(myfile.read())


myfile.seek(0)


myfile.read()

myfile.seek(0)

myfile.readlines()


with open('myfile.txt') as my_file:
    content=my_file.read()
 

print(content)


with open('myfile.txt',mode='a') as f:
    f.write("\none one three")



myfile.seek(0)
myfile.read()


with open('myfile.txt') as my_file:
    content=my_file.read()
    print(content)


print(content)
