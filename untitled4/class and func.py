class ClassName:
    pass
instance = ClassName()
class Students:
    def _init_(self, name,age,grade):
                self.name = name
                self.age = age
                self.grade = grade

student1 = Students("bob", 12,"7th")

class Students:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        def displaystudents(self):
            return("Stuient name is "+ self.name +