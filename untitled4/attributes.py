#class Students:
    #def _init_(self,name,age):
       # self.name = name
        #self.age = age

#student1 = Students("Fred", 17)
#student2 = Students("Mike",12)
#setattr(student1,"grade",'8th')
#hasattr(student1,"grade")
#delattr(student2,"age")
class ClassName:
    pass
instance = ClassName()
class Students:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

student1 = Students("Bob",12,"7th")

#class Over writting
class Parent:
    def func(self):
        print("This is a child function")

c = ClassName()
c.func()

        