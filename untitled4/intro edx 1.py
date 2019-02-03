counter = 0
while counter<100:
    if counter==4:
        break
    else:
        pass
    print(counter)
    counter = counter+1

    for i in "PYTHON":
        if i == "h":
            continue
            print(i)


for i in range(0,5):
    if i < 2:
        continue
        print(i)


#Try and except
#try to acess data through python

try:
    if name>3:
        print("Hi")

except:
    print("Python ran into an error")


#Classs

c

class Students:
    def__init__(self,name,age):
    self.name = name
    self.age

class Studnets:
    def__init__(self,name,age):
    self.name=name
    self.age = age


student1=Students("Fred",17)
student2=Students("Mike",12)
setattr(student1,"grade","8th") #sets attribute to the fuction
hasattr(student1,"grade")
getattr(student1,"grade") # calling atribute
delattr(student1,"grade") #to delete an attribute
hasattr(student1,"grade") 3to check if attribute exists



