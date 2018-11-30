from types import MethodType
class Student(object):
    pass

    


s = Student()
s.name = 'nametest'
print(s.name)


def set_age(self,age):
    self.age = age

s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)